class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    ptr = Node(data)
    ptr.next = head
    return ptr

def build_one_two_three():
    head = Node(None)
    ptr = head
    for i in range(0, 3):
        ptr.next = Node(i + 1)
        ptr = ptr.next
    return head.next