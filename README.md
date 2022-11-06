# whispertoy

Playing around with OpenAI's Whisper model.

## Prerequisites

- [Poetry](https://python-poetry.org/)
- [FFmpeg](https://ffmpeg.org/) *(e.g. `sudo apt install ffmpeg`)*
- [Rust](https://www.rust-lang.org/tools/install)
- [PortAudio](http://portaudio.com/) *(e.g. `sudo apt install libportaudio2`)*

## Dev setup

```sh
poetry shell
poetry install
```

## Determine correct sound device

```sh
python -m sounddevice
```
