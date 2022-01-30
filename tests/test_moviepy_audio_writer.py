from unittest import mock

import pytest
from video_speak_extractor import MoviePyAudioWriterAdapter

input_file = "test.mkv"
output_file = "test.mp3"
start = "1"
end = "4"


def test_MoviePyAudioWriter_write_calls_audio_writer_with_rigth_params():
    sut = MoviePyAudioWriterAdapter
    sut._audio_writer = mock.Mock()
    sut.write(input_file, output_file, start, end)

    sut._audio_writer.assert_called_with(input_file)


def test_MoviePyAudioWriter_write_calls_write_audiofile_with_rigth_params():
    audio_writer = mock.Mock()
    sut = MoviePyAudioWriterAdapter
    sut._audio_writer = audio_writer

    sut.write(input_file, output_file, start, end)

    audio_writer().subclip().write_audiofile.assert_called_with(output_file)


@pytest.mark.parametrize("start", ["", False])
def test_MoviePyAudioWriter_write_returns_false_when_receive_start_with_invalid_values(  # noqa: E501
    start,
):
    audio_writer = mock.Mock()
    sut = MoviePyAudioWriterAdapter
    sut._audio_writer = audio_writer

    assert sut.write(input_file, output_file, start, end) is False


@pytest.mark.parametrize("end", ["", False])
def test_MoviePyAudioWriter_write_returns_false_when_receive_end_with_invalid_values(  # noqa: E501
    end,
):
    audio_writer = mock.Mock()
    sut = MoviePyAudioWriterAdapter
    sut._audio_writer = audio_writer

    assert sut.write(input_file, output_file, start, end) is False
