import LinkedBinaryTree

def is_height_balanced(bin_tree):
    helper_result = is_height_balanced_helper(bin_tree.root)
    return helper_result[1]


def is_height_balanced_helper(bin_tree_subroot):
    if (bin_tree_subroot.left is None and bin_tree_subroot.right is None):
        return (1, True) # (height, is balanced)
    elif (bin_tree_subroot.left is None): # left is 0
        # check the height of right
        right = is_height_balanced_helper(bin_tree_subroot.right)
        if (right[0] > 1 or right[1] == False):
            return (right[0] + 1, False)
        else:
            return (right[0] + 1, True)
    elif (bin_tree_subroot.right is None): # right is 0
        # check the height of left
        left = is_height_balanced_helper(bin_tree_subroot.left)
        if (left[0] > 1 or left[1] == False):
            return (left[0] + 1, False)
        else:
            return (left[0] + 1, True)
    else: # has two children
        left = is_height_balanced_helper(bin_tree_subroot.left)
        right = is_height_balanced_helper(bin_tree_subroot.right)
        height_diff = abs(left[0] - right[0])
        if (height_diff > 1 or left[1] == False or right[1] is False):
            return (left[0] + right[0], False)
        else:
            return (left[0] + right[0], True)


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
    print(is_height_balanced(my_bin_tree))


#main()
