from abc import ABC, abstractmethod


class PluginABC(ABC):
    """
    This is an Abstract Base class to Plugins
    """

    @abstractmethod
    def execute(self, *args, **kwargs) -> bool:
        """
        This can receive any args and the implementation
        will handle this.

        This concrete implementation should overwrite this

        Returns:
            bool: True if have the success. Otherwhise returns False
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.order})"
