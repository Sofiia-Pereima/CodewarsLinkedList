class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return head
    head1 = Node(None)
    ptr = head
    ptr1 = head1
    while ptr.next is not None:
        if ptr.data != ptr.next.data:
            ptr1.next = Node(ptr.data)
            ptr1 = ptr1.next
        ptr = ptr.next
    if ptr.data != ptr1.data:
        ptr1.next = Node(ptr.data)
    return head1.next
