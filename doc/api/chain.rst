Chain
=====
Blockchain is in fact what stored in ``Storage``. But handling operations like
traversing the chain and verifying blocks is not the idea of desiging storage.
To make some higher level operations and make a unified source of truth,
``Chain`` class is placed between storage and higher level class that do the
main job.

.. autoclass:: pyzantium.Chain
   :members:
