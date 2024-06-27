#!/usr/bin/python3
"""
class VerboseList
"""


class VerboseList(list):
    """
    VerboseList extends the built-in list class
    to provide custom notifications
    when items are added or removed from the list.
    """

    def append(self, item):
        """
        Appends an item to the list and prints
        a notification message.
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """
        Extends the list with items from the iterable
        and prints a notification message.
        """
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """
        Removes the first occurrence of an item from
        the list and prints a notification message.
        """
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns the item at the given index,
        or the last item if no index is specified,
        and prints a notification message.
        """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
