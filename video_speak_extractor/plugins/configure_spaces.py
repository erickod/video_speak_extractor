import re
from typing import Any

from video_speak_extractor import PluginABC


class ConfigureSpacesPlugin(PluginABC):
    plugin_type = "content"
    is_enabled = True
    order = 3

    @classmethod
    def execute(cls, *args, **kwargs) -> Any:
        speak = kwargs["speak"]
        speak["content"] = re.sub(
            r"@{1,}",
            " ",
            speak["content"],
        )
        return speak