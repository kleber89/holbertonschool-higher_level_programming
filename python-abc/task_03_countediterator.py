#!/usr/bin/python3
"""
A CountedIterator class that wraps an iterator
and keeps track of the number of items yielded.
"""


class CountedIterator:
    """
    CountedIterator extends the built-in iterator
    to keep track of the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and the counter.

        Parameters:
        iterable (iterable): The iterable to be wrapped by the CountedIterator.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.

        Returns:
        The next item from the iterator.

        Raises:
        StopIteration: When there are no more items to iterate over.
        """
        item = next(self.iterator)  # This will raise StopIteration if no items are left
        self.counter += 1
        return item

    def get_count(self):
        """
        Returns the number of items that have been iterated over.

        Returns:
        int: The count of items iterated.
        """
        return self.counter
