"""
Linked List Stringification Module.
"""
def stringify(node):
    """
    Converts a singly linked list into a formatted string.
    """
    res = []
    while node:
        res.append(node.data)
        node = node.next
    res.append('None')
    return ' -> '.join(res)
