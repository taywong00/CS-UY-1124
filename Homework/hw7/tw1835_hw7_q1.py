import LinkedBinaryTree

# implementaion notes:
# 1. cannot use LinkedBinaryTree methods


def min_and_max(bin_tree):
    if (bin_tree.size == 0): # is empty
        raise EmptyCollection('Linked Binary Tree is empty')

    def subtree_min_and_max(subtree_root):
        if (subtree_root.left is None and subtree_root.right is None): # no children
            return (subtree_root.data, subtree_root.data)
        elif (subtree_root.left is None):
            right = subtree_min_and_max(subtree_root.right) # (min, max)
            return (min(right[0], subtree_root.data), max(right[1], subtree_root.data))
        elif (subtree_root.right is None):
            left = subtree_min_and_max(subtree_root.left)
            return (min(left[0], subtree_root.data), max(left[1], subtree_root.data))
        else: # has two children
            left = subtree_min_and_max(subtree_root.left) # (min, max)
            right = subtree_min_and_max(subtree_root.right)
            return (min(left[0], right[0], subtree_root.data), max(left[1], right[1], subtree_root.data))

    return subtree_min_and_max(bin_tree.root)


def main():
    node31 = LinkedBinaryTree.LinkedBinaryTree.Node(5)
    node32 = LinkedBinaryTree.LinkedBinaryTree.Node(1)
    node21 = LinkedBinaryTree.LinkedBinaryTree.Node(9, node31, node32)
    node22 = LinkedBinaryTree.LinkedBinaryTree.Node(8)
    node23 = LinkedBinaryTree.LinkedBinaryTree.Node(4)
    node11 = LinkedBinaryTree.LinkedBinaryTree.Node(2, node21)
    node12 = LinkedBinaryTree.LinkedBinaryTree.Node(7, node22, node23)
    node01 = LinkedBinaryTree.LinkedBinaryTree.Node(3, node11, node12)
    my_bin_tree = LinkedBinaryTree.LinkedBinaryTree(node01)
    print(min_and_max(my_bin_tree))


#main()
