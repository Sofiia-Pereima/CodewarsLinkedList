def stringify(node):
    ptr = node
    result = ''
    while ptr != None:
        result += str(ptr.data) + ' -> '
        ptr = ptr.next
    result += 'None'
    return result