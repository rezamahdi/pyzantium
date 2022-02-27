from abc import ABC
from abc import abstractmethod
from datetime import datetime
from typing import Generator


class Block:
    """
    Programatical representation of a block in a chain

    This class is just and abstraction of block. just holds neccesary
    information and data about a block. Instanteniation of this class doesn't
    mean that this block is part of a chain, in fact it is a data class.
    """

    def __init__(self) -> None:
        self._hash: bytes = bytes()
        self._prev_hash: bytes = bytes()
        self._nonce: int = None
        self._timestamp: datetime = None
        self._data = None

    def __eq__(self, other: object) -> bool:
        # comparing hashes is enough
        if isinstance(other, Block):
            return self._hash == other._hash
        raise TypeError(
            "Object of type {} is not a Block or subclass of it".format(other.__class__)
        )


class BlockSerializer(ABC):
    """
    An abstract base class to serialize a block to variuse types

    Using data stored in a block involves converting it to some specific
    bytes data. Specialy when it is needed to hash it. ``Block`` class is just a
    data holder and to produce flattened raw byte, an other class is needed to
    convert it.
    """

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def to_storing(self) -> Generator[bytes, None, None]:
        """
        Converts the given block to a format ready to store in the storage

        :rtype Generator:
        """
        ...

    @abstractmethod
    def to_finilizing(self) -> Generator[bytes, None, None]:
        """
        Converts the given block to a format to use in finalizing operation

        :rtype Generator:
        """
        ...
