from pytest import mark, fixture
import hashlib


@fixture
def chain():
    return 1


class TestBlock:
    def test_create_block(chain):
        assert 1 == 1
