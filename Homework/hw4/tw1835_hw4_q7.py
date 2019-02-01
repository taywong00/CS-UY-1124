def split_by_sign(lst, low, high):
    # given list, int, int
    # reorder the elements so negatives come before positive

    # base case: only one elem in the list, sorted
    if (high - low == 0):
        return [lst[low]]

    # recursive case: 2+ elements in the list
    # takes 2 sorted lists
    else:
        curr_val = lst[low]

        if (lst[low] > 0): # positive
            ret_lst = split_by_sign(lst, low + 1, high) + [curr_val]
            print (ret_lst)

        else: # negative
            ret_lst = [curr_val] + split_by_sign(lst, low + 1, high)
            print (ret_lst)
        return ret_lst

print(split_by_sign([-4, 27, -420, -236, 4, 6, 8], 0, 6))
