import LinkedBinaryTree

# create and returns a new tree built from the prefix expression
def create_expression_tree(prefix_exp_str):
    prefix_list = prefix_exp_str.split()
    operators = '+-*/'
    # start from the back and find the pos of the first operator
    start_pos = len(prefix_list) - 1
    for i in range(start_pos):
        if (prefix_list[start_pos] in operators):
            break
        else:
            start_pos -= 1
    helper_res = create_expression_tree_helper(prefix_list, 0)
    ret_tree = LinkedBinaryTree.LinkedBinaryTree(helper_res[0])
    return ret_tree


# reutrn (subtree created, size of the subtree-- to determine the new start pos)
# starts at the inner most subtree
def create_expression_tree_helper(prefix_exp, start_pos):
    operators = '+-*/'

    if (prefix_exp[start_pos] not in operators):
        new_node = LinkedBinaryTree.LinkedBinaryTree.Node(int(prefix_exp[start_pos]))
        return (new_node, 1)

    else: # is an operator
        left = create_expression_tree_helper(prefix_exp, start_pos + 1)
        right = create_expression_tree_helper(prefix_exp, start_pos + 1 + left[1])
        subtree = LinkedBinaryTree.LinkedBinaryTree.Node(prefix_exp[start_pos], left[0], right[0])
        total_size = left[1] + right[1] + 1
        return (subtree, total_size)


def prefix_to_postfix(prefix_exp_str):
    prefix_tree = create_expression_tree(prefix_exp_str)
    ret_str = ''
    for item in prefix_tree.postorder():
        ret_str += str(item.data) + ' '
    return ret_str



def main():
    prefix_exp = '* 2 + - 15 6 4'
    new_tree = create_expression_tree(prefix_exp)

    for item in new_tree.preorder():
        print(item.data, end=' ')
    print()
    print(prefix_to_postfix(prefix_exp))
#main()
