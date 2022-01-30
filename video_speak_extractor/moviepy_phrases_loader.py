import logging
from typing import Dict, Generator, List, Union

from moviepy.video.tools.subtitles import SubtitlesClip


class MoviePyPhrasesLoader:
    subtitles_clip = SubtitlesClip

    @classmethod
    def load_phrases(
        cls, **kwargs
    ) -> Generator[Dict[str, Union[str, List[str]]], None, None]:
        logging.warning("asdfasdfasdfasdfasdf")

        punctuation: str = ".?!"
        speaks: List[Dict[str, Union[str, List[str]]]] = [
            {"speaks": [], "start": "", "end": "", "content": ""}
        ]

        for section in cls.subtitles_clip(kwargs["file"]):
            speaks[-1]["speaks"].append(section[1] + "  ")  # type: ignore

            if not speaks[-1]["start"]:
                speaks[-1]["start"] = str(section[0][0])

            if section[1][-1] in punctuation:
                speaks[-1]["end"] = str(section[0][1])
                speaks[-1]["content"] = "".join(speaks[-1]["speaks"])

                yield speaks[-1]

                speaks.append(
                    {
                        "speaks": [],
                        "start": "",
                        "end": "",
                        "content": "",
                    }
                )
