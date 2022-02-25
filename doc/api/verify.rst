Verifying
=========
An important concept in blockchain is the authority of data that are stored in
the blocks. Common scheme to verify authority of data in blockchain is using
Elliptic Curve Cryptography (ECC), but other types of authority checking schemes
are applicable.

Verifying authority in pyzantium is implemented using an interface called
``Verifier``. currently ECC is implemented using Cryptography package. you can
add your own scheme of verifying by sublassing ``Verifier`` and implemente
``verify`` method to return ``True`` when data authority is approved and return
``Flase`` otherwise.

.. autoclass:: pyzantium.verify.Verifier
   :members:

Elliptic curve verification is implementation using ``ECCVerifier`` class:

.. autoclass:: pyzantium.verify.ECCVerifier

Someone may don't need verification at all. So using ``VoidVerifier`` is the answer:

.. autoclass:: pyzantium.verify.VoidVerifier