import importlib
import os
import re
from typing import Any, List


class PluginLoader:
    excluded = ["__init__.py", "__pycache__", "PluginABC"]
    plugins_dir = "video_speak_extractor.plugins"

    @classmethod
    def load_plugins(cls, plugin_type: str) -> List[Any]:
        plugins_module = importlib.import_module(
            cls.plugins_dir,
        )

        plugin_list = []
        for f in os.listdir(
            getattr(plugins_module, "__file__").replace("__init__.py", "")
        ):

            if f in cls.excluded:
                continue

            if plugin := cls.__get_plugin_from_module(
                f.replace(".py", ""), plugin_type=plugin_type
            ):
                plugin_list.append(plugin())

        return sorted(plugin_list, key=lambda x: x.order)

    @classmethod
    def __get_plugin_from_module(cls, plugin_name: str, plugin_type: str) -> Any:
        module = importlib.import_module(
            f"{cls.plugins_dir}.{plugin_name}",
        )
        for name in dir(module):
            if name in cls.excluded or re.match("__.*__", name):
                continue

            if (
                (plugin := getattr(module, name))
                and hasattr(plugin, "is_enabled")
                and plugin.is_enabled
                and plugin.plugin_type.lower() == plugin_type.lower()
            ):
                return plugin
