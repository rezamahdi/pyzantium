from abc import ABC, abstractmethod
from typing import Any

from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


class Verifier(ABC):
    """
    Abstract base class for validating data.

    This class provide an interface for data verifiers to verify data that
    will append to a block.
    """

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def verify(self, data: bytes) -> bool:
        """
        Checks verify (Authority) of data

        :param data: Data that will be added to block
        :return: True if signature is ok, False otherwise
        """
        ...


class ECCVerifier(Verifier):
    """
    Data verifier using ECC

    This verifier checks validity based on a digital signature produced by an
    Elliptic curve.

    :param pkey: Elliptic curve public key of author
    :param hash: Hash algorithm used to generate signature
    :param signature: Signature of this data
    """

    def __init__(
        self, pkey: ec.EllipticCurvePublicKey, hash: hashes.Hash, signature: bytes
    ) -> None:
        super().__init__()
        self._pkey = pkey
        self._hash = hash
        self._signature = signature

    def verify(self, data: bytes) -> bool:
        hasher = hashes.Hash(self._hash)

        # TODO: hash data with chunks
        hasher.update(data)
        digest = hasher.finalize()

        dsa = ec.ECDSA(utils.Prehashed(hasher))

        try:
            self._pkey.verify(self._signature, digest, dsa)
        except InvalidSignature:
            return False

        return True


class VoidVerifier(Verifier):
    """
    This is an empty verifier that will say data is valid allwasy

    This class is not intendet to be used in production. Using this verifier
    will cause to ignore validity of data.
    """

    def __init__(self) -> None:
        super().__init__()

    def verify(self, data: bytes) -> bool:
        return True
