import BinarySearchTreeMap

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap.BinarySearchTreeMap()
    for item in prefix_lst:
        bst[item] = None
    return bst

def main():
    restored_bst = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
    for key in restored_bst:
        print (key)

#main()






































#
#
#
# def restore_bst(prefix_lst):
#     bst = BinarySearchTreeMap.BinarySearchTreeMap()
#     root_item = BinarySearchTreeMap.BinarySearchTreeMap.Item(prefix_lst[0])
#     root_node = BinarySearchTreeMap.BinarySearchTreeMap.Node(root_item)
#     restore_bst_helper(bst, prefix_lst, 0, root_node)
#
#
#
# def restore_bst_helper(bst, prefix_lst, curr_ind, parent_node):
#     # base case
#     if ():
#         data_key = prefix_lst[curr_ind]
#         data_item = BinarySearchTreeMap.BinarySearchTreeMap.Item(data_key)
#         data_node = BinarySearchTreeMap.BinarySearchTreeMap.Node(data_item)
#         ...
#         ...
#         return (data_node, 1)
#
#     # recursive case
#     data_key = prefix_lst[curr_ind]
#     data_item = BinarySearchTreeMap.BinarySearchTreeMap.Item(data_key)
#     data_node = BinarySearchTreeMap.BinarySearchTreeMap.Node(data_item)
#
#     left_tuple = restore_bst_helper(bst, prefix_lst, curr_ind + 1) # (left_node, num nodes in subtree)
#     num_nodes_in_left = left_tuple[1]
#     right_tuple = restore_bst_helper(bst, prefix_lst, curr_ind + num_nodes_in_left + 1) (right_node, num_nodes_in_right)
#     num_nodes_in_right = right_tuple[1]
#
#     left_node = left_tuple[0]
#     right_node = right_tuple[0]
#
#     data_node.left = left_node
#     left_node.parent = data_node
#     data_node.right = right_node
#     right_node.parent = data_node
#
#     total_curr_tree_size = num_nodes_in_left + num_nodes_in_right + 1
#
#     return (data_node, total_curr_tree_size)
#
#
#
#






#
#
# '''
# def restore_bst(prefix_lst):
#     bst = BinarySearchTreeMap.BinarySearchTreeMap()
#     root_item = BinarySearchTreeMap.BinarySearchTreeMap.Item(prefix_lst[0])
#     root_node = BinarySearchTreeMap.BinarySearchTreeMap.Node(item)
#     parent_node = root_node
#     parent_val = parent_node.item.key
#     for ind in range(1, len(prefix_lst)):
#         new_val = prefix_lst[ind]
#         new_item = BinarySearchTreeMap.BinarySearchTreeMap.Item(new_val)
#         new_node = BinarySearchTreeMap.BinarySearchTreeMap.Node(new_item)
#         if (curr < parent_val):
#             parent_node.left = new_node
#             new_node.parent = parent_node
#             parent_node = new_node
#         else:
#             # curr parent is a leaf
#
#             # curr parent is NOT leaf, this should be the right node
#
# '''
# def restore_bst(prefix_lst):
#     bst = BinarySearchTreeMap.BinarySearchTreeMap()
#     restore_bst_helper(bst, prefix_lst, curr_ind)
#     return bst
#
#
# def restore_bst_helper(bst, prefix_lst, curr_ind):
#     data_key = prefix_lst[curr_ind]
#     data_item = BinarySearchTreeMap.BinarySearchTreeMap.Item(data_key)
#     data = BinarySearchTreeMap.BinarySearchTreeMap.Node(item)
#
#     if (curr_ind == len(prefix_lst) - 1): # curr_ind is the last item in the list
#         return data
#
#     else: # there are still more to compare to after
#         next_key = prefix_lst[curr_ind + 1]
#         if (next_key < data_key): # next goes left
#             left = restore_bst_helper(bst, prefix_lst, curr_ind + 1)
#             right = restore_bst_helper(bst, prefix_lst, curr_ind + len(left))
#
#             data.left = left
#             left.parent = data
#             data.right = right
#             right.parent = data
#
#         else:
#             right = restore_bst_helper(bst, prefix_lst, curr + 1)
#             data.right
#
#
# # note: maybe try a for loop with a non-recursive helper function
