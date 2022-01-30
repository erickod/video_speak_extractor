from typing import Dict, Generator, List, Protocol, Union, runtime_checkable


@runtime_checkable
class IPhrasesLoader(Protocol):
    @classmethod
    def load_phrases(
        cls,
        **kwargs,
    ) -> Generator[Dict[str, Union[str, List[str]]], None, None]:
        pass
