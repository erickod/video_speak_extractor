from unittest import mock

from video_speak_extractor import MoviePyPhrasesLoader


def test_load_phrases_method_calls_subtitles_clip_with_right_params():
    MoviePyPhrasesLoader.subtitles_clip = mock.MagicMock(
        return_value=[((1, 2), "Some phrase.")]
    )
    list(MoviePyPhrasesLoader.load_phrases(file="test.srt"))
    MoviePyPhrasesLoader.subtitles_clip.assert_called_with("test.srt")
