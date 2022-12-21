import pytest

from pennsieve2 import Pennsieve


def test_alive():
    p = Pennsieve(connect=False)
    assert 1 == 1
