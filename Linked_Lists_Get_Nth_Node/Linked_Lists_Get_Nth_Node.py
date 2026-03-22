"""
This module provides functionality for working with linked lists.
It includes a custom exception class for handling index errors
and a function to retrieve a specific node by its index.
"""
from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

class IndexError(BaseException):
    """Custom exception for invalid linked list indices or empty lists."""
    def __init__(self, text):
        """Initializes the exception with an error message."""
        self.text = text
    def __str__(self):
        """Returns the string representation of the error message."""
        return self.text


def get_nth(node, index):
    """
    Retrieves the node at the specified index in a linked list.
    Raises IndexError if the index is out of bounds or the list is empty.
    """
    if node is None:
        raise IndexError('None linked list should throw error.')
    if index < 0:
        raise IndexError('Invalid index value should throw error.')
    while index > 0:
        try:
            node = node.next
        except AttributeError:
            raise IndexError('Invalid index value should throw error.')
        if node is None:
            raise IndexError('Invalid index value should throw error.')
        index -= 1
    return node
