class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if head is None:
        return Node(data)
    if data < head.data:
        ptr = Node(data)
        ptr.next = head
        return ptr
    ptr = head
    while data >= ptr.data and ptr.next is not None and ptr.next.data < data:
        ptr = ptr.next 
    if ptr.next is None:
        ptr.next = Node(data)
    else:
        temp = Node(data)
        temp.next = ptr.next
        ptr.next = temp
    return head
