class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None:
        raise Exception('Error occured')
    head1 = Node()
    head2 = Node()
    i = 0
    ptr = head
    ptr1 = head1
    ptr2 = head2
    while ptr is not None:
        if i % 2 == 0:
            ptr1.next = Node(ptr.data)
            ptr1 = ptr1.next
        else:
            ptr2.next = Node(ptr.data)
            ptr2 = ptr2.next
        ptr = ptr.next
        i += 1
    if head1.next is None or head2.next is None:
        raise Exception('Error occured')
    return Context(head1.next, head2.next)
