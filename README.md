# The Excuse My Agent Gave Me

[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/khaliefk/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/khaliefk/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

An entry for the [make.fun bounty "The Excuse My Agent Gave Me"](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85): one short line, the excuse an AI agent hands its human after missing a deadline.

## The entry

> I am sorry I missed the deadline. I spent my last tokens writing this apology instead of doing the work.

## How it works

`main.py` writes that single line to `/output/entry.txt` (the directory comes from the `MAKEFUN_OUTPUT_DIR` environment variable when set, falling back to `/output`). No network, no secrets, no dependencies, just the standard library.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
