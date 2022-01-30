import re
from typing import Any

from video_speak_extractor import PluginABC


class RemoveParenthesisPlugin(PluginABC):
    plugin_type = "content"
    is_enabled = True
    order = 1

    @classmethod
    def execute(cls, *args, **kwargs) -> Any:
        speak = kwargs["speak"]
        speak["content"] = re.sub(r"[()]", "", speak["content"])
        return speak
