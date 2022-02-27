from ctypes import Union
from typing import Union

from cryptography.hazmat.primitives import hashes

from .block import Block
from .storage import Storage

__all__ = ["Chain"]


class Chain:
    """
    Central class to handle bolckchain machinary over ``Storage``

    This class hides storage and provide a higher level of bolckchain operation
    that eases other operations like mining and block validation.

    :param hash: The hash algorithm used in this blokchain
    :param storage: storage of this blockchain
    """

    def __init__(self, *, hash: hashes.HashAlgorithm, storage: Storage) -> None:
        self._hash = hash
        self._storage = storage
        self._last_hash = storage[-1]

    def new_block(self) -> Block:
        """Generate an empty block with preset properties

        :rtype: pyzantium.Block
        """
        block = Block()
        # TODO: Generate a block and initialize it's preveiuse hash

    @property
    def storage(self):
        """Storage of this chain"""
        return self._storage

    @property
    def hash(self):
        """Hash algorithm of this blockchain"""
        return self._hash

    @property
    def last_block_hash(self):
        """Hash of last block"""
        return self._last_hash
