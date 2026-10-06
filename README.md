# random-everyday-stuff

A grab bag of small scripts for everyday tasks.

## Setup

Requires Python 3.11+.

```sh
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

## Tools

| Script | What it does |
| --- | --- |
| [qr_gen.py](qr_gen.py) | Generates a QR code PNG for a URL |

### qr_gen.py

Creates a QR code image from a URL. If the URL has no scheme, `https://` is added.

Running `python qr_gen.py` directly generates a QR code for the URL hard-coded at the bottom of the file.
