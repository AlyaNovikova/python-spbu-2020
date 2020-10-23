from hypothesis import given
import hypothesis.strategies as st
from my_array import Array


def to_tuple(array):
    return tuple(iter(array))


@given(st.integers(), st.integers())
def test_init(x, y):
    assert to_tuple(Array()) == tuple()
    assert to_tuple(Array(x)) == (x,)
    assert to_tuple(Array(x, y)) == (x, y)


@given(st.integers(), st.integers())
def test_iter(x, y):
    list_from_array = []
    for element in Array(x, y):
        list_from_array.append(element)
    assert list_from_array == [x, y]


@given(st.integers(), st.integers())
def test_append(x, y):
    array = Array(x)
    array.append(y)
    array.append(x)
    assert to_tuple(array) == (x, y, x)


@given(st.integers(), st.integers(), st.integers())
def test_add(x, y, z):
    array1 = Array(x)
    array2 = Array(y, z)
    assert array1 + array2 == Array(x, y, z)


@given(st.integers())
def test_len(x):
    array = Array()
    assert len(array) == 0

    for _ in range(10):
        array.append(x)
    assert len(array) == 10


@given(st.integers(), st.integers())
def test_index(x, y):
    array = Array(x, y, x)
    assert array.index(x) == 0
    assert array.index(y) == 1 or x == y


@given(st.integers(), st.integers(), st.integers())
def test_pop(x, y, z):
    array = Array(x, y, y, z)
    array.pop(1)
    assert to_tuple(array) == (x, y, z)

    array.pop(array.index(x))
    assert to_tuple(array) == (y, z)


@given(st.integers(), st.integers())
def test_remove(x, y):
    array = Array(x, x, y, x)
    array.remove(x)
    print(array._data)
    assert to_tuple(array) == (x, y, x)

    array.remove(y)
    assert to_tuple(array) == (x, x)

    array.remove(x)
    assert to_tuple(array) == (x,)




