"""Linked list utilities for pushing nodes and building a specific list."""
from preloaded import Node

# Node is defined in preloaded like this:

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


def push(head, data):
    """
    Pushes a new node with the given data to the front of the list.
    """
    new_head = Node(data)
    new_head.next = head
    return new_head

def build_one_two_three():
    """
    Builds a linked list with the values 1 -> 2 -> 3 -> None.
    """
    head = None
    for i in [3 ,2, 1]:
        head = push(head, i)
    return head
