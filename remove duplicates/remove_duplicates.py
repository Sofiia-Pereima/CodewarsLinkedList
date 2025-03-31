class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# def push(head, data):
#     ptr = Node(data)
#     ptr.next = head
#     return ptr

# def stringify(node):
#     ptr = node
#     result = ''
#     while ptr is not None:
#         result += str(ptr.data) + ' -> '
#         ptr = ptr.next
#     result += 'None'
#     return result

# def build_list(lst):
#     head = Node(None)
#     ptr = head
#     for el in lst:
#         ptr.next = Node(el)
#         ptr = ptr.next
#     return head.next

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

# t = build_list([1, 2, 3, 3, 4, 4, 5])
# print(stringify(t))
# p = remove_duplicates(build_list([1, 1, 1]))
# print(stringify(p))