from __future__ import annotations

import math
import struct
import wave
from pathlib import Path


class TextToSpeech:
    """TTS interface."""

    def speak(self, text: str, out_path: Path) -> Path:
        raise NotImplementedError


class OfflineStubTTS(TextToSpeech):
    """
    Offline TTS that writes a short audible tone (not silence) so the
    sign→voice pipeline produces a real playable WAV without native engines.
    """

    def speak(self, text: str, out_path: Path) -> Path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        duration_sec = min(3.0, 0.35 + 0.07 * max(1, len(text.split())))
        sample_rate = 16000
        n_samples = int(sample_rate * duration_sec)
        # simple multi-beep mapping from text length
        freq = 220 + (len(text) % 12) * 40
        frames = bytearray()
        for i in range(n_samples):
            t = i / sample_rate
            # envelope to avoid clicks
            env = min(1.0, t * 10) * min(1.0, (duration_sec - t) * 10)
            # soft square-ish tone
            val = env * 0.25 * math.sin(2 * math.pi * freq * t)
            frames += struct.pack("<h", int(val * 32767))
        with wave.open(str(out_path), "w") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(bytes(frames))
        out_path.with_suffix(".txt").write_text(text, encoding="utf-8")
        return out_path


def get_default_tts() -> TextToSpeech:
    return OfflineStubTTS()
