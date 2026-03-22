"""Module for parsing string representations into linked lists."""
from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    """
    Parses a formatted string into a linked list of Nodes.
    """
    if list_repr == 'None':
        return None
    data = list_repr.split(' -> ')
    head = Node(int(data[0]))
    current = head
    for el in data[1:-1]:
        current.next = Node(int(el))
        current = current.next
    return head
