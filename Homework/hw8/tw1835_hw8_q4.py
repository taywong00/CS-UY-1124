import BinarySearchTreeMap

def find_min_abs_difference(bst):
    compare_diff_tuple = find_min_abs_difference_helper(bst.root)
    return compare_diff_tuple[0]

def find_min_abs_difference_helper(subtree_root): # recursive, returns tuple (difference, compare value)
    ## print('curr node', subtree_root.item.key)

    # if leaf (no children)
    if (subtree_root.left is None and subtree_root.right is None):
        # handle difference
        official_difference = None # (not 0 because 0 < 1, and min difference ever has to be 1-- no duplicates)

        # handle compare value
        # compare value = curr node
        compare_value = subtree_root.item.key


    # has LEFT child
    elif (subtree_root.right is None):
        # get data from the left child
        left_child = find_min_abs_difference_helper(subtree_root.left) # curr.left -- (left diff, left compare)
        ## print(subtree_root.item.key, '\'s left child', left_child)

        # handle difference value
        # if child's difference is None
        if (left_child[0] == None):
            # automatically use the difference between you and the child
            # so:
            # difference = abs(curr - left)
            official_difference = abs(subtree_root.item.key - left_child[1]) # curr val - left compare val
        else: # (child has a difference)
            # get the difference between you and the child
            curr_left_difference = abs(subtree_root.item.key - left_child[1]) # curr val - left compare val
            # send the smaller difference (your's and the childs or just the child's)
            # official difference = min(your and left's  difference, left's difference)
            official_difference = min(curr_left_difference, left_child[0])


        # handle compare value
        # if root (no parent)
        if (subtree_root.parent is None):
            # send self
            compare_value = subtree_root.item.key
        # if curr is a left child
        elif (subtree_root.parent.left is subtree_root):
            # send curr as compare value (closest to parent)
            # compare value = curr
            compare_value = subtree_root.item.key
        # if curr is a right child
        else:
            # send left child as compare value (closest to parent)
            # compare value = left
            compare_value = left_child[1]



    # has RIGHT child
    elif (subtree_root.left is None):
        # get data from the right child
        right_child = find_min_abs_difference_helper(subtree_root.right)
        ## print(subtree_root.item.key, '\'s right child', right_child)

        # hadnle difference value
        # if child's difference is None
        if (right_child[0] == None):
            # automatically use the difference between you and the child
            # so:
            # difference = abs(curr - right)
            official_difference = abs(subtree_root.item.key - right_child[1])
        else: # (child has a difference)
            # get the difference between you and the child
            curr_right_difference = abs(subtree_root.item.key - right_child[1])
            # send the smaller difference (your's and the child's or just the child's)
            # official difference = min(you and the right's difference, right's difference)
            official_difference = min(curr_right_difference, left[0])


        # handle the compare value
        # if root (no parent)
        if (subtree_root.parent is None):
            # send self
            compare_value = subtree_root.item.key
        # if curr is a left child
        elif (subtree_root.parent.left is subtree_root):
            # send right child as compare value
            compare_value = right_child[1]
        # if curr is a right child
        else:
            # send curr as a compare value (closest to the parent)
            compare_value = subtree_root.item.key



    # has BOTH children
    else:
        # get data from both children
        left_child = find_min_abs_difference_helper(subtree_root.left)
        right_child = find_min_abs_difference_helper(subtree_root.right)

        ## print(subtree_root.item.key, '\'s left child', left_child)
        ## print(subtree_root.item.key, '\'s right child', right_child)

        # handle the difference value
        # if BOTH children's differences are None
        if (left_child[0] == None and right_child[0] == None):
            # get the difference between curr and left
            # curr left = abs(curr - left)
            curr_left_difference = abs(subtree_root.item.key - left_child[1])
            # get the difference between curr and right
            # curr right = abs(curr - right)
            curr_right_difference = abs(subtree_root.item.key - right_child[1])
            # send the min of those differences (dont have to worry about comparing with the children's differences)
            # official difference = min(curr left difference, curr right difference)
            official_difference = min(curr_left_difference, curr_right_difference)

        # if LEFT child's difference is None (only right child has a differece)
        elif (left_child[0] == 0):
            # get the difference between you and both the children
            # curr left = abs(curr - left)
            curr_left_difference = abs(subtree_root.item.key - left_child[1])
            # curr right = abs(curr - right)
            curr_right_difference = abs(subtree_root.item.key - right_child[1])
            # make the official difference the min of curr/left, curr/right, and right
            # official difference = min(curr/left diff, curr/right diff, right diff)
            official_difference = min(curr_left_difference, curr_right_difference, right_child[0])

        # if RIGHT child's difference is None (only left child has a difference)
        elif (right_child[0] == 0):
            # get the difference between you and both children
            # curr left = abs(curr - left)
            curr_left_difference = abs(subtree_root.item.key - left_child[1])
            # curr right = abs(curr - right)
            curr_right_difference = abs(subtree_root.item.key - right_child[1])
            # make the official difference between curr/left, curr/right, and left diff
            # official difference = min(curr/left, curr/right, left diff)
            official_difference = min(curr_left_difference, curr_right_difference, left_child[0])

        # if BOTH children have valid differences
        else:
            # get the difference between you and both children
            # curr left = abs(curr - left)
            curr_left_difference = abs(subtree_root.item.key - left_child[1])
            # curr right = abs(curr - right)
            curr_right_difference = abs(subtree_root.item.key - right_child[1])
            # make the official difference between curr/left, curr/right, left diff, and right diff
            # official difference (curr/left, curr/right, left, right)
            official_difference = min(curr_left_difference, curr_right_difference, left_child[0], right_child[0])



        # handle compare value
        # if root (no parent)
        if (subtree_root.parent is None):
            # send self
            compare_value = subtree_root.item.key
        # if curr is a left child, send curr's right child
        # if curr's parent's left child is curr (curr is a left child)
        elif (subtree_root.parent.left is subtree_root):
            # compare value = curr's right child (closest to curr's parent)
            compare_value = right_child[1]
        # if curr is a right child, send curr's left child
        # if curr's parent's right child is curr (curr is a right child)
        else:
            # compare value = curr's left child (closest to curr's parent)
            compare_value = left_child[1]

    ## print('exit', subtree_root.item.key)

    return (official_difference, compare_value)






def main():
    bst = BinarySearchTreeMap.BinarySearchTreeMap()
    bst[9] = None
    bst[7] = None
    bst[3] = None
    bst[1] = None
    bst[5] = None
    bst[13] = None
    bst[11] = None
    bst[15] = None

    print(find_min_abs_difference(bst))

#main()
