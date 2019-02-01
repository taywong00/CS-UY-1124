# maybe change to be more like merge sort?

def list_min(lst, low, high):
    # given list of ints, 2 ints (range of indices for the list)
    # recursively find an return the min elem between low-high

    # base case: only considering 1 item
    if (high - low == 0):
        # print('min val: ', lst[low])
        return lst[low]

    # recursive case
    else:
        if (lst[low] <= lst[high]):
            return list_min(lst, low, high - 1)
        else:
            return list_min(lst, low + 1, high)


def main():
    mylst = [5, 3, 65, 7, 3, 1, 8, 9, 4, 6]
    print (list_min(mylst, 2, 8))
    print (list_min2(mylst, 2, 8))


main()
