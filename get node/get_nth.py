class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def get_nth(node, index):
    if index < 0:
        raise Exception('Error occured')
    ptr = node
    i = 0
    while ptr is not None and i < index:
        ptr = ptr.next
        i += 1
    if ptr is None:
        raise Exception('Error occured')
    if ptr is not None:
        return ptr
