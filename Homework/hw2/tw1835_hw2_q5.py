def split_parity(lst):
    # takes list of ints
    # changes lst: odd numbers first, even numbers after (order doesnt matter)
    # runtime: n
    partition = 0
    for curr_pos in range(len(lst) - 1):
        if (lst[curr_pos] % 2 != 0): # is odd
            #swap with the first value outside the "good section", the partition
            curr_elem = lst[curr_pos]
            partition_elem = lst[partition]
            lst[partition] = curr_elem
            lst[curr_pos] = partition_elem
            partition += 1 # increment partition so the odd num is in the "good section"

    return

def main():
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lst1)

    split_parity(lst1)

    print('new list: ', lst1)

#main()
