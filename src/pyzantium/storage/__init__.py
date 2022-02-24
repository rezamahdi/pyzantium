from abc import ABC, abstractmethod


class Storage(ABC):
    """
    Abstract base class for storage mechanisms

    All storage mechanisms must implement this base class.
    This class provides an abstraction to separate storage from higher level
    blockchain machinary. Note that objects of ``Storage``'s subclass
    is not intended to be used directly by user.

    :param name: Name of storage. This name is not name of blockchain it is
                 just a name for storage class.
    :type name: str
    """

    def __init__(self, name: str) -> None:
        super().__init__()

    @abstractmethod
    def __getitem__(self, hash: bytes):
        ...

    @abstractmethod
    def __contains__(self, hash: bytes) -> bool:
        ...

    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self):
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...


from .disk import DiskStorage
