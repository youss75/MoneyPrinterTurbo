"""Create initial Novelbeat preferences without replacing an existing config."""
from pathlib import Path

import toml


def configure(root: Path) -> bool:
    target = root / "config.toml"
    if target.exists():
        print("Existing config.toml preserved; see novelbeat/README.md for preferences.")
        return False
    data = toml.load(root / "config.example.toml")
    data["listen_host"] = "127.0.0.1"
    data["app"].update(video_source="local", subtitle_provider="edge")
    data.setdefault("ui", {}).update(
        language="en", video_language="hi", video_aspect_local="9:16",
        video_concat_mode="sequential", video_clip_duration=8,
        video_clip_speed=1.0, video_count=1,
        tts_server="azure-tts-v1", voice_name="hi-IN-SwaraNeural-Female",
        voice_rate=1.0, voice_volume=1.0, bgm_type="", bgm_volume=0.0,
        subtitle_enabled=False,
    )
    with target.open("x", encoding="utf-8") as output:
        toml.dump(data, output)
    print("Novelbeat config created: local clips, Hindi voice, vertical video.")
    return True


if __name__ == "__main__":
    configure(Path(__file__).resolve().parents[1])
