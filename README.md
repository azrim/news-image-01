# news-image-01

Entry for make.fun bounty [news-image-01](https://make.fun): **"Sum up 13 November's world news in one image"**.

The program writes a deterministic newspaper-style poster (`/output/entry.png`)
summarizing eight AP wire stories from 13 November 2026. All bytes are embedded
in `main.py` — no network, no randomness, identical output on every run.

## Run

```sh
python main.py   # writes /output/entry.png (override dir with MAKEFUN_OUTPUT_DIR)
```

License: MIT
