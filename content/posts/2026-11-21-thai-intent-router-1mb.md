---
title: How a 1.1 MB offline Thai intent router works
date: 2026-11-21
summary: TER-AI's router reads one Thai or Thai-English message with typos and returns one of 15 intents in well under a millisecond on a CPU. No GPU, no network, no dependencies. Here is the whole pipeline.
---
Most Thai chatbot demos send every message to a large model. For commands like "what time is it", "add these numbers" or "stop", that is slow, needs a network, and costs money. The intent router in [TER-AI](https://github.com/klanarongz2009-sketch/ter-ai) does that one job offline: Thai or Thai-English text in, one of 15 intents out. The model file is 1.1 MB and inference is pure Python.

You can try it in the browser on the [demo page](https://klanarongz2009-sketch.github.io/ter-ai/), or locally:

```bash
pip install git+https://github.com/klanarongz2009-sketch/ter-ai.git
terai "เส็ดหรือยัง"
```

```
status    1.00  normalized: เสร็จหรือยัง
```

The input has a typo (`เส็ด` for `เสร็จ`, "finished"). The router fixes it and answers `status`. Here is how.

## Step 1: fix the typos you know about

Thai typing has typos that repeat: a dropped tone mark, the wrong one of two consonants that sound the same, a missing silent letter. The normalizer runs three steps in a fixed order:

1. **Context rules** for typos that are only safe in some places. `ท่า` is a real word, so it only becomes `ถ้า` ("if") at the start of a word, where the rule says so.
2. **A typo table**, longest entry first: `เส็ด` to `เสร็จ`, `พิมพิด` to `พิมพ์ผิด`, `ขอโทด` to `ขอโทษ`, 75 safe pairs in all. An entry is skipped when the match already sits inside the correct word, so `พิม` inside `พิมพ์` is left alone.
3. **Collapse long repeats**: a character typed four or more times becomes one, so `อีกแล้ววววว` becomes `อีกแล้ว`.

The table only holds pairs where the typed form is not a correct word itself. A typo that is also a real word needs a context rule, or it would break correct text.

## Step 2: a phonetic skeleton for the typos you do not know

A table never covers every typo. So the router also builds a second, looser version of the text, the *skeleton*: tone marks and silent marks are dropped, consonants that sound the same are merged, and long and short vowels are merged. Two examples from the real code:

- `เส็ด` and `เสด` both become `เสด`
- `ค่ะ` and `คะ` both become `คะ`

The skeleton is not shown to the user. It is only used as extra features, so a typo that is not in the table still lands close to the right word. `เสดยัง` (not in the table) still routes to `status`, with confidence 0.92.

## Step 3: character n-grams instead of words

Thai is written without spaces between words, and word segmentation is itself a model that can be wrong on typos. The router skips it. After normalizing, it also folds digits (`15+27` and `๑๕+๒๗` look the same to the model) and spaces, then takes:

- every character n-gram of length 1 to 4 of the normalized text, and
- every character n-gram of length 2 to 4 of the skeleton.

Each distinct n-gram counts once. This works the same for Thai, English, and a mix of both, so `help me หน่อย` needs no special handling.

## Step 4: a linear classifier with int8 weights

The classifier is a linear softmax model: one weight per feature per intent, plus a bias per intent. It was trained on 32,604 rows. After dropping rare features, 32,367 features remain. Each weight is stored as one signed byte with one shared scale, base64 encoded in a JSON file. That is where the 1.1 MB comes from.

At run time:

1. Look up each n-gram in the vocabulary.
2. Add up its 15 weights.
3. Apply the scale and bias, then softmax.

No matrix library is needed, so the same integer arithmetic runs in JavaScript on the demo page, and a parity check in the repo confirms that the browser and Python give the same answers.

The result also reports **coverage**: the share of the input's features the model has seen before. A message like `xyz qqq` gets a coverage of 0.05, which tells the calling app that this is probably not a command at all, even though some intent has to come out on top.

## How well it works, and where it fails

On the project's frozen test set of 124 sentences it gets 97.6% (121/124), and 99.1% (111/112) on a held-out set, at about 0.2 ms per message on one CPU thread. These are internal evaluations with sets the project made itself, not an independent benchmark.

The three test-set misses are all short English questions:

- `what is my name` goes to `set_name` instead of `get_name`
- `do you know my name` goes to `who`
- `pick a number` goes to `set_name` instead of `random`

English is the weak side, because most of the training data is Thai. Fixing that without leaking test sentences into training data is an open [help wanted issue](https://github.com/klanarongz2009-sketch/ter-ai/issues/21).

## Why build it this way

- **It runs with very little.** Any machine with Python 3.11, or a browser tab through the JavaScript port. Nothing to download at run time.
- **It is easy to fix.** A wrong typo fix is one line in a JSON table. A wrong intent can be traced to the n-grams that pushed it there.
- **It does one job.** Send commands to fixed handlers, and send everything else to a bigger model only when you need one.

## Help wanted

If you work with Thai text, there are small, clear tasks to start with: [add tests for typo pairs](https://github.com/klanarongz2009-sketch/ter-ai/issues/19), [document the examples](https://github.com/klanarongz2009-sketch/ter-ai/issues/20), or [improve English routing](https://github.com/klanarongz2009-sketch/ter-ai/issues/21). Read [CONTRIBUTING.md](https://github.com/klanarongz2009-sketch/ter-ai/blob/main/CONTRIBUTING.md) first. I am a boarding-school student, so replies can take days.

Code is MIT. The optional Thai voice weights in the same repo use a non-commercial license; the router does not use them.
