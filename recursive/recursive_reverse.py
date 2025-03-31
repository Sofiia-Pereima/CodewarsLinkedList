class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None or head.next is None:
        return head

    ptr = head
    while ptr.next is not None and ptr.next.next is not None:
        ptr = ptr.next

    temp = ptr.next
    ptr.next = None

    if temp is not None:
        new_head = reverse(head)
        temp.next = new_head
        return temp

    return None
