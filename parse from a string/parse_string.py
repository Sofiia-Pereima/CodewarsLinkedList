class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    head = Node(None, None)
    ptr = head
    arr = s.split(' -> ')
    for i in range(len(arr) - 1):
        ptr.next = Node(int(arr[i]), None)
        ptr = ptr.next
    return head.next
