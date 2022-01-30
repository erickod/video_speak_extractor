import click

from video_speak_extractor import (
    Coordinator,
    MoviePyAudioWriterAdapter,
    MoviePyPhrasesLoader,
)


@click.command()
@click.option("--video", default="", help="Video path")
@click.option("--srt", default="", help=".srt path")
@click.option(
    "--output-dir",
    default="",
    help="Directory to write the audio and txt files",
)
def extract(video: str, srt: str, output_dir: str):
    """
    Reads a .srt file extracting phrases, splitting the video's
    audio to match the .srt phrases and export them to output_dir.
    """

    if not video or not srt or not output_dir:
        help_msg = extract.get_help(click.get_current_context())
        click.echo(help_msg)
        return

    Coordinator(
        phrases_loader=MoviePyPhrasesLoader,
        audio_writer=MoviePyAudioWriterAdapter,
        output_dir=output_dir,
    ).execute(srt, video)
