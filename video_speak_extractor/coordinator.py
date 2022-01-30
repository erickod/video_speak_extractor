import os
import re

from .moviepy_audio_writer import MoviePyAudioWriterAdapter
from .moviepy_phrases_loader import MoviePyPhrasesLoader
from .plugin_loader import PluginLoader
from .protocols import IAudioWriter, IPhrasesLoader


class Coordinator:
    _plugin_loader = PluginLoader

    def __init__(
        self,
        *,
        phrases_loader: IPhrasesLoader = MoviePyPhrasesLoader(),
        audio_writer: IAudioWriter = MoviePyAudioWriterAdapter(),
        output_dir: str,
    ) -> None:
        splited_path = re.split("\\|/", output_dir)
        export_dir_name = "export"

        self._output_dir = (
            os.path.join(*splited_path)
            if output_dir.endswith(export_dir_name)
            else os.path.join(*splited_path, export_dir_name)
        )
        self._phrases_loader = phrases_loader
        self._audio_writer = audio_writer

    def execute(
        self,
        phrase_file: str,
        video_file: str,
    ) -> None:

        for i, speak in enumerate(
            self._phrases_loader.load_phrases(file=phrase_file),
        ):
            if speak and speak["start"] and speak["end"]:
                for plugin in self._plugin_loader.load_plugins("content"):
                    plugin.execute(speak=speak)

                filename: str = re.sub(" ", "_", str(speak["content"]))
                filename = re.sub("[\\.,!:'\";]?", "", filename)
                speak_dir = os.path.join(
                    self._output_dir,
                    f"{i} - {filename[0:50]}",
                )
                os.makedirs(speak_dir, exist_ok=True)
                output_file = os.path.join(speak_dir, f"{filename[:50]}.mp3")
                self.write_file(speak, f"{output_file}.txt")
                self._audio_writer.write(
                    video_file,
                    output_file,
                    speak["start"],  # type: ignore
                    speak["end"],  # type: ignore
                )

    def write_file(self, speak, output_dir: str) -> None:
        with open(output_dir, "w") as f:
            f.write(speak["content"])
