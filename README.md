# Loru

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.2.1-0E8A16.svg)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MergeOS](https://img.shields.io/badge/MergeOS-bounties-5319E7.svg)](https://github.com/mergeos-bounties)

**Loru** is an offline **sign language** toolkit: landmark sequences → gloss/text, and sign → **voice (WAV)** — demos and train loops without a GPU requirement for the smoke path.

Product: [mergeos-bounties/Loru](https://github.com/mergeos-bounties/Loru)

---

## Table of contents

- [Highlights](#highlights)
- [Screenshots](#screenshots)
- [Quick start](#quick-start)
- [CLI reference](#cli-reference)
- [Data & pipeline](#data--pipeline)
- [Diagrams](#diagrams)
- [Architecture](#architecture)
- [Development](#development)
- [MergeOS bounties](#mergeos-bounties)
- [License](#license)

---

## Highlights

| Mode | Description |
| --- | --- |
| **Sign → text** | Landmark JSON sequences → gloss / sentence |
| **Sign → voice** | Recognition + TTS-style WAV export |
| **Offline demo** | Samples, toy train, infer `hello` end-to-end |
| **Gloss vocab** | Default gloss set for demos |
| **Serve** | Optional FastAPI for integrations |

---

## Screenshots

| Pipeline | Samples |
| :---: | :---: |
| ![Sign→voice](docs/screenshots/demo-sign-to-voice.png) | ![Samples](docs/screenshots/demo-samples.png) |
| *Offline sign → text → voice* | *Gloss sample catalog* |

---

## Quick start

```powershell
cd Loru
python -m venv .venv
.\.venv\Scripts\activate
pip install -e ".[dev]"

loru version
loru data list
loru demo
```

Demo writes audio under the configured output directory (e.g. `demo_hello.wav`).

---

## CLI reference

| Command | Purpose |
| --- | --- |
| `loru version` | Version + demo gloss vocab |
| `loru demo` | Train smoke + infer text + voice on `hello` |
| `loru data list` | Landmark sample files |
| `loru infer demo -s hello` | Gloss → sentence |
| `loru infer text …` | Sign file → text |
| `loru train` / `eval` | Toy train + evaluation |
| `loru serve` | Optional API |

```powershell
loru infer demo --sign thank_you
loru demo
```

---

## Data & pipeline

```text
samples (JSON landmarks)
        │
        ▼
  toy train / vocab
        │
        ├─► sign_to_text  → gloss / sentence
        └─► sign_to_voice → WAV path
```

| Path | Content |
| --- | --- |
| Samples | `SAMPLES_DIR` landmark sequences |
| Outputs | `OUT_DIR` audio + reports |

Respect consent and privacy for real sign recordings; demos use synthetic/offline fixtures.

---


## Diagrams

System architecture and workflow — shown full-width below.  
Open the HTML files for **dark/light theme toggle** and export (PNG/SVG).

### Architecture

[Open interactive diagram](docs/diagrams/architecture.html)

<p align="center">
  <img src="docs/diagrams/architecture.svg" alt="Architecture diagram" width="100%" />
</p>

### Workflow

[Open interactive diagram](docs/diagrams/workflow.html)

<p align="center">
  <img src="docs/diagrams/workflow.svg" alt="Workflow diagram" width="100%" />
</p>

*Generated with [archify](https://github.com/tt-a1i).*

## Architecture

```text
src/loru/
  cli.py
  infer/          # text, voice, pipeline
  data/loader.py
  models/vocab.py
  train/toy_train.py
docs/screenshots/
```

---

## Development

```powershell
pytest -q
ruff check src tests
loru demo
```

---

## MergeOS bounties

High demand: **sign packs** (gloss + evidence photo/video + consent).  
Star repos → claim issue → PR to **master** → MRG **25–200**.

---

## Tiếng Việt

**Loru** nhận diện ký hiệu → chữ / giọng (offline demo). Chạy: `loru demo`.

---

## License

MIT · MergeOS / ThanhTrucSolutions
