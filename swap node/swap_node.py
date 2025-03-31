class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data
        
def linked_list_from_string(s):
    head = Node(None, None)
    ptr = head
    arr = s.split(' -> ')
    for i in range(len(arr)):
        ptr.next = Node(None, arr[i])
        ptr = ptr.next
    return head.next

def stringify(node):
    ptr = node
    result = ''
    while ptr is not None:
        result += str(ptr.data) + ' -> '
        ptr = ptr.next
    result += 'None'
    return result
        
def swap_pairs(head):
    f = Node(Node())
    f.next = head
    head = f
    ptr = f
    while (ptr is not None) and (ptr.next is not None) and (ptr.next.next is not None):
        print(ptr.data)
        ptr1 = ptr.next 
        ptr.next = ptr1.next 
        # ptr1.next.next = ptr1
        # ptr1.next = ptr.next.next 
        ptr1.next = ptr.next.next
        ptr.next.next = ptr1
        print('z = ', ptr.next.data)
        print('k = ', ptr.next.next.data)
        ptr = ptr.next
        ptr = ptr.next
        print('p = ', ptr.data)
    head = head.next
    return head
    

l = linked_list_from_string('A -> B -> C')
print(stringify(l))
s = swap_pairs(l)
print(stringify(s))