def stringify(node):
    ptr = node
    result = ''
    while ptr is not None:
        result += str(ptr.data) + ' -> '
        ptr = ptr.next
    result += 'None'
    return result
