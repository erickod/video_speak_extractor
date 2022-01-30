import os
from unittest import mock

from video_speak_extractor import (
    Coordinator,
    MoviePyAudioWriterAdapter,
    MoviePyPhrasesLoader,
)

speak = {"start": "00", "end": "01", "content": "any valid content"}


def test_coordinator_can_be_imported() -> None:
    assert Coordinator


def test_coordinator_has_default_params_when_instantiated() -> None:
    sut = Coordinator(output_dir="any valid output dir")
    assert sut._phrases_loader
    assert sut._audio_writer


def test_coordinator_save_some_constructor_attr_as_its_param() -> None:
    sut = Coordinator(
        audio_writer=MoviePyAudioWriterAdapter(),
        phrases_loader=MoviePyPhrasesLoader(),
        output_dir="any valid output dir",
    )
    assert isinstance(sut._phrases_loader, MoviePyPhrasesLoader)
    assert isinstance(sut._audio_writer, MoviePyAudioWriterAdapter)


def test_coordinator_output_dir_attribute() -> None:
    sut = Coordinator(
        output_dir="root_dir",
    )
    assert sut._output_dir == os.path.join("root_dir", "export")


@mock.patch("os.makedirs")
def test_coordinator_execute_calls_write_method(mocked_os) -> None:
    sut = Coordinator(
        output_dir="root_dir",
    )
    sut.write_file = mock.Mock()  # type: ignore
    sut._audio_writer = mock.Mock()
    sut._phrases_loader = mock.MagicMock()
    sut._phrases_loader.load_phrases.return_value = [speak]

    sut.execute("subtitles.srt", "video.mp4")

    sut._audio_writer.write.assert_called_with(
        "video.mp4",
        "root_dir/export/0 - any_valid_content/any_valid_content.mp3",
        speak["start"],
        speak["end"],
    )


@mock.patch("os.makedirs")
def test_coordinator_execute_calls_load_phrases(mocked_os) -> None:
    sut = Coordinator(
        output_dir="root_dir",
    )
    sut.write_file = mock.Mock()  # type: ignore
    sut._audio_writer = mock.Mock()
    sut._phrases_loader = mock.MagicMock()
    sut._phrases_loader.load_phrases.return_value = [speak]

    sut.execute("subtitles.srt", "video.mp4")

    sut._phrases_loader.load_phrases.assert_called()


@mock.patch("os.makedirs")
def test_coordinator_execute_calls_write_file(mocked_os) -> None:
    sut = Coordinator(output_dir="root_dir")

    sut.write_file = mock.Mock()  # type: ignore
    sut._audio_writer = mock.Mock()
    sut._phrases_loader = mock.MagicMock()
    sut._phrases_loader.load_phrases.return_value = [speak]

    sut.execute("subtitles.srt", "video.mp4")

    sut.write_file.assert_called_with(
        speak,
        "root_dir/export/0 - any_valid_content/any_valid_content.mp3.txt",
    )


@mock.patch("builtins.open")
def test_write_file_calls_open_with_right_params(mopen):
    sut = Coordinator(output_dir="root_dir")
    sut.write_file(speak, "output_dir")
    mopen.assert_called()
