import pytest

from numpy.testing import assert_raises
import array_api_strict as xp
import numpy as np

@pytest.mark.parametrize(
    "from_, to, expected",
    [
        (xp.int8, xp.int16, True),
        (xp.int16, xp.int8, False),
        (xp.bool, xp.int8, False),
        (xp.asarray(0, dtype=xp.uint8), xp.int8, False),
    ],
)
def test_can_cast(from_, to, expected):
    """
    can_cast() returns correct result
    """
    assert xp.can_cast(from_, to) == expected

def test_isdtype_strictness():
    assert_raises(TypeError, lambda: xp.isdtype(xp.float64, 64))
    assert_raises(ValueError, lambda: xp.isdtype(xp.float64, 'f8'))

    assert_raises(TypeError, lambda: xp.isdtype(xp.float64, (('integral',),)))
    assert_raises(TypeError, lambda: xp.isdtype(xp.float64, np.object_))

    assert_raises(TypeError, lambda: xp.isdtype(xp.float64, None))
    assert_raises(TypeError, lambda: xp.isdtype(xp.float64, np.float64))
