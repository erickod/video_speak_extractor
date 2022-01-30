from typing import Dict, List, Protocol, Union, runtime_checkable


@runtime_checkable
class IAudioWriter(Protocol):
    @classmethod
    def write(cls, input_file: str, output_file: str, start: str, end: str) -> bool:
        raise NotImplementedError
