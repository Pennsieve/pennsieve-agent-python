import pytest

from pennsieve import Pennsieve


def test_alive():
    p = Pennsieve(connect=False)
    assert 1 == 1
