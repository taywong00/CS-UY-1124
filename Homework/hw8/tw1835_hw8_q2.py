import BinarySearchTreeMap

def create_chain_bst(n):
    bst = BinarySearchTreeMap.BinarySearchTreeMap()
    for num in range(1, n + 1):
        bst[num] = None
    return bst


def create_complete_bst(n):
    bst = BinarySearchTreeMap.BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high): # recursive
    if (low == high):
        item = BinarySearchTreeMap.BinarySearchTreeMap.Item(low)
        node = BinarySearchTreeMap.BinarySearchTreeMap.Node(item)

    else:
        mid = (low + high) // 2
        item = BinarySearchTreeMap.BinarySearchTreeMap.Item(mid)
        node = BinarySearchTreeMap.BinarySearchTreeMap.Node(item)

        left = add_items(bst, low, mid - 1)
        right = add_items(bst, mid + 1, high)

        node.left = left
        left.parent = node
        node.right = right
        right.parent = node

        if (bst.is_empty()):
            bst.root = node

    return node


# not finished, analyze the runtime

def main():
    bst1 = create_chain_bst(4)
    indent = ''
    for node in bst1:
        print(indent, node)
    #
        indent += '   '

    bst2 = create_complete_bst(7)
    print(bst2.root)
    for node in bst2:
        print(node)

#main()
