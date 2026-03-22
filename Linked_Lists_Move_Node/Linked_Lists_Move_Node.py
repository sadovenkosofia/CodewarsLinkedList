"""
This module provides classes and functions for manipulating linked lists,
specifically for moving a node from the head of one list to another.
"""
class Node(object):
    """Represents a single node in a linked list."""
    def __init__(self, data):
        """Initializes a new node with the specified data and no next node."""
        self.data = data
        self.next = None

class Context(object):
    """Stores the state of two linked lists (source and destination)."""
    def __init__(self, source, dest):
        """Initializes the context with the updated source and destination lists."""
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Moves the head node from the source list to the head of the destination list.
    Returns a Context object containing both updated lists.
    """
    el = source
    source = source.next

    res = Node(el)
    res.next = dest
    dest = res
    return Context(source, dest)
