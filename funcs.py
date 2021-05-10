from collections import deque, defaultdict
from itertools import count
from typing import Iterable, Any, Tuple, Optional


def ilen1(iterable: Iterable) -> int:
    """Функция получения размера генератора
    >>> foo = (x for x in range(10))
    >>> ilen1(foo)
    10
    """
    return sum(1 for _ in iterable)


def ilen2(iterable: Iterable) -> int:
    """Функция получения размера генератора
    >>> foo = (x for x in range(10))
    >>> ilen2(foo)
    10
    """
    return len(list(iterable))


def ilen3(iterable: Iterable) -> int:
    """Функция получения размера генератора
    >>> foo = (x for x in range(10))
    >>> ilen3(foo)
    10
    """
    counter = count()
    deque(zip(iterable, counter), maxlen=0)
    return next(counter)


def flatten(iterable: Iterable[Any]) -> Iterable[Any]:
    """Делает из многоуровневого массива одноуровневый
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    for i in iterable:
        if isinstance(i, (list, set, frozenset, tuple)):
            yield from flatten(i)
        elif isinstance(i, (int, str, float, bool)):
            yield i
        else:
            raise ValueError(f'Unsupported type: {type(i)}')


def distinct(iterable: Iterable[Any]) -> Iterable[Any]:
    """Удалит дубликаты, сохранив порядок
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    non_unique = set()
    for i in iterable:
        if i not in non_unique:
            yield i
            non_unique.add(i)


def groupby(key, iterable: Iterable[dict]) -> dict:
    """Упорядочивает неупорядоченную последовательность из словарей, группируя их по ключу
    >>> users = [
    ... {'gender': 'female', 'age': 33},
    ... {'gender': 'male', 'age': 20},
    ... ]
    >>> groupby('gender', users)
    {'female': [{'gender': 'female', 'age': 33}], 'male': [{'gender': 'male', 'age': 20}]}

    >>> groupby('age', users)
    {33: [{'gender': 'female', 'age': 33}], 20: [{'gender': 'male', 'age': 20}]}
    """
    out = defaultdict(list)
    for d in iterable:
        out[d.get(key, None)].append(d)
    return dict(out)


def chunks(size: int, iterable: Iterable[Any]) -> Iterable[Tuple[Any, ...]]:
    """Разбивает последовательность на заданные куски
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4)]
    """
    iterator = iter(iterable)
    chunk = []
    try:
        while True:
            for i in range(size):
                chunk.append(next(iterator))
            yield tuple(chunk)
            chunk = []
    except StopIteration:
        yield tuple(chunk)


def first(iterable: Iterable[Any]) -> Optional[Any]:
    """Возвращает первый элемент в последовательности или None
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0))
    """
    try:
        return next(iter(iterable))
    except StopIteration:
        return


def last(iterable: Iterable[Any]) -> Optional[Any]:
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0))
    """
    iterator = iter(iterable)
    i = None
    try:
        while True:
            i = next(iterator)
    except StopIteration:
        return i
