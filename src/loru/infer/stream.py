"""Continuous multi-gloss stream stub (phrase building)."""

from __future__ import annotations

from loru.infer.text import gloss_to_sentence, multi_gloss_to_sentence
from loru.models.vocab import DEFAULT_GLOSS


def stream_glosses(glosses: list[str]) -> dict:
    """
    Accept a sequence of gloss tokens and emit progressive sentence states.

    This is a scaffold for a future continuous recognizer that emits partial
    glosses over time (e.g. webcam frames). Offline and deterministic.
    """
    cleaned: list[str] = []
    for g in glosses:
        key = str(g).strip().lower().replace(" ", "_")
        if not key:
            continue
        if key not in DEFAULT_GLOSS:
            # allow unknown tokens as raw words for streaming demos
            cleaned.append(key)
        else:
            cleaned.append(key)

    partials: list[dict] = []
    acc: list[str] = []
    for g in cleaned:
        acc.append(g)
        partials.append(
            {
                "glosses": list(acc),
                "sentence": multi_gloss_to_sentence(acc),
                "last_gloss_sentence": gloss_to_sentence(g),
            }
        )
    return {
        "ok": True,
        "n": len(cleaned),
        "final_sentence": multi_gloss_to_sentence(cleaned) if cleaned else "",
        "stream": partials,
        "mode": "continuous-gloss-stub",
    }
