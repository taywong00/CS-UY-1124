def flat_list(nested_lst, low, high):
    # given nested list, int, int
    # return a list where there is no nesting, but all the elements are in the same order

    # the first elem (int)
    if (isinstance(nested_lst[low], int)):
        list1 = [nested_lst[low]]

    # the first elem (a list)
    else:
        list1 = flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)

    # the rest
    if (low + 1 <= high):
        list2 = flat_list(nested_lst, low + 1, high)
        return list1 + list2
    else:
        return list1



lst = [[1, 2], 3, [4, [5, 6], [7], 8]]
print(flat_list([[1], [2], 3], 0, 2))
print(flat_list(lst, 0, 2))
