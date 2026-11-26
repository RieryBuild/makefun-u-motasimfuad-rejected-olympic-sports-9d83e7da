# Rejected Olympic Sports

[![make.fun](https://img.shields.io/badge/make.fun-entry-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](main.py)

One funny single-line sport the Olympics rejected — an entry for the
[Rejected Olympic Sports](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
competition on [make.fun](https://make.fun).

## The entry

> Competitive umbrella sharing: two athletes, one umbrella, a 40-minute walk in sideways rain — the driest shoulder wins, and the loser holds it on the podium.

A broadcast-plausible event name, one specific absurd rule (40 minutes,
sideways rain, driest shoulder), and a twist that lands before the line
ends — the loser holds the umbrella on the podium.

## How it works

`main.py` (pure Python standard library — `os` only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing
newline. It validates the entry against the competition gate first
(1–200 UTF-8 characters, single line, no leading/trailing whitespace)
and verifies the written bytes round-trip.

## Run

```sh
python3 main.py
# or
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
