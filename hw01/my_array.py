"""Implementation of class Array based on tuple."""


class Array(object):  # noqa: WPS214
    """Class for storing items with list interface."""

    __slots__ = ('_data',)

    def __init__(self, *init_elements):
        """
        Initialize an array with a list of elements.

        :param init_elements: elements to be initialized
        """
        self._data = tuple(init_elements)  # noqa: WPS110

    def __iter__(self):
        """
        Return an iterator of the array.

        Needed, for example, to work with a loop `for`.

        :return: array iterator
        """
        return iter(self._data)

    def append(self, new_element):
        """
        Add a new object inside the array.

        :param new_element: the object to add
        """
        self._data = (*self._data, new_element)  # noqa: WPS110

    def __add__(self, other):
        """
        Add two arrays.

        Forming an array consisting of the elements of both arrays.

        :param other: array to be added
        :return: returns the resulting array of the sum
        """
        return Array(*self, *other)

    def __len__(self):
        """
        Count the number of elements in an array.

        :return: array length
        """
        return len(self._data)

    def index(self, element):
        """
        Find the index of the passed object.

        Returns -1 if there is no such object in the array.

        :param element: the object to find the index of
        :return: the index of the object or -1 if there is no such object
        """
        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def __getitem__(self, index):
        """
        Get the value by index using [].

        :param index: element index
        :return: element by index
        """
        return self._data[index]

    def pop(self, index):
        """
        Remove element at index.

        If the index is out of range, then throw IndexError.

        :param index: index of element to remove
        :raises IndexError: if the index is out of range(0, len(array))
        """
        if index < 0 or index >= len(self):
            raise IndexError
        self._data = self._data[:index] + self._data[index + 1:]  # noqa: WPS110

    def remove(self, element):
        """
        Find the first occurrence of the element in the array and removes it.

        If the element is not in the array, then throw ValueError.

        :param element: the value of the element to be removed
        :raises ValueError: if the value is not in the array
        """
        element_index = self.index(element)
        if element_index == -1:
            raise ValueError
        self._data = self.pop(element_index)  # noqa: WPS110

    def __eq__(self, other: 'Array'):
        """
        Compare whether values in two arrays are equal.

        :param other: the array to compare against
        :return: bool: True if the arrays are equal and False otherwise
        """
        return self._data == tuple(*iter(other))
