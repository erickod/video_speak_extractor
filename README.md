# video_speak_extractor

## Why did it was made?
This was made to help me learning foreign languages using videos. That way, this cli reads a .srt file extracting phrases, splitting the video's audio to match  the phrases and exporting them to a gave directory.

## How to use it?
1. Clone this repository;
2. Make sure you have poetry installed;
3. Execute `poetry install` inside the directory that contains `pyproject.toml` file.
4. Execute `poetry build` inside the same directory said above.
5. Inside the .whl file with pip, that it is inside the dist directory.

This will expose a video2phrases command with below options:

```
Usage: main.py [OPTIONS]

  Reads a .srt file extracting phrases, spliting the video's video to match
  the .srt phrases and export them to output_dir.

Options:
  --video TEXT       Video path
  --srt TEXT         .srt path
  --output-dir TEXT  Directory to write the audio and txt files
  --help             Show this message and exit.
```