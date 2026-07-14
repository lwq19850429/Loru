# Demo sample sequences

Synthetic landmark JSON for the offline toy classifier.

| Field | Meaning |
| --- | --- |
| `gloss` | Isolated sign label |
| `frames` | List of frames; each frame is a list of `[x,y,z]` landmarks |
| `language` | `demo-asl` for scaffold only |
| `source` | `synthetic-scaffold` — not real signer video |

These are **not** real sign language recordings. Replace with consented / licensed corpora via bounties.

## Cycle 2026-07-14b

Ensure every `DEFAULT_GLOSS` entry has a matching `samples/<gloss>.json`. Run `loru data coverage` (or vocab coverage CLI) after adding samples.
