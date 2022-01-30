from moviepy.editor import AudioFileClip


class MoviePyAudioWriterAdapter:
    _audio_writer = AudioFileClip

    @classmethod
    def write(
        cls,
        input_file: str,
        output_file: str,
        start: str,
        end: str,
    ) -> bool:
        if not start or not end:
            return False
        clip = cls._audio_writer(input_file).subclip(start, end)
        clip.audio_fadein(0.2)
        clip.audio_fadeout(0.2)
        clip.write_audiofile(output_file)

        return True
