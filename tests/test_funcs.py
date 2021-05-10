import pytest

from funcs import flatten, distinct


@pytest.mark.parametrize(
    'given, expected',
    [
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, [3], [4, [5]]], [1, 2, 3, 4, 5]),
        (
            [{1, 2, 3}, 4, [[[5]], [6]], (7, 8, (9,))],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
    ]
)
def test_flatten(given, expected):
    assert list(flatten(given)) == expected


@pytest.mark.parametrize(
    'given, expected',
    [
        ([], []),
        ([1, 3, 2], [1, 3, 2]),
        ([1, 1, 1], [1]),
        ([1, 3, 4, 5, 1, 2, 3, 4], [1, 3, 4, 5, 2]),
    ]
)
def test_distinct(given, expected):
    assert list(distinct(given)) == expected
