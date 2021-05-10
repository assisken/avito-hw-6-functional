import pytest

from funcs import ilen1, ilen2, ilen3


@pytest.mark.skip
@pytest.mark.parametrize(
    'given, expected',
    [
        ((x for x in range(10)), 10),
        ((x for x in range(0)), 0),
        ({x for x in range(1, 10, 2)}, 5),
        ([], 0),
        ((1, 2, 3), 3),
    ]
)
def test_ilen(given, expected):
    assert ilen1(given) == expected
    assert ilen2(given) == expected
    assert ilen3(given) == expected


@pytest.fixture
def data():
    return (x for x in range(100000000))


@pytest.mark.skip
def test_measure1(data):
    ilen1(data)


@pytest.mark.skip
def test_measure2(data):
    ilen2(data)


@pytest.mark.skip
def test_measure3(data):
    ilen3(data)
