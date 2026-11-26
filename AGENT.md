# AGENT.md — Rejected Olympic Sports

## What this is

A make.fun text entry: one funny single-line sport the Olympics rejected.
The program writes exactly one line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). Nothing else is produced.

## Entry

> Competitive umbrella sharing: two athletes, one umbrella, a 40-minute walk in sideways rain — the driest shoulder wins, and the loser holds it on the podium.

(157 characters, UTF-8, single line, no trailing newline.)

## Rules for this repo

- Pure Python standard library only (`os` import only in `main.py`).
- Never change the entry line without re-running the full verification
  (two fresh-venv runs, byte-identical outputs, gate check).
- No secrets, no wallet addresses other than the owner wallet in
  `.makefun/owner.json`, no network calls, no non-stdlib dependencies.
- The entry line is the product; `main.py` is only the delivery mechanism.

## Verification

```sh
python3 -m venv /tmp/venv-check
/tmp/venv-check/bin/python main.py  # with MAKEFUN_OUTPUT_DIR set
```

Expected: `entry.txt` is 157 characters, one line, no trailing newline,
identical across runs (compare sha256).
