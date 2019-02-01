def two_sum(srt_lst, target):
    # srt_lst: a list of sorted ints
    # an int
    # returns tuple of indices (x, y) where
    #   srt_lst[x] + srt_lst[y] = target
    # is this never works out: returns None
    # runtime: AIM FOR n
    lower = 0
    upper = len(srt_lst) - 1
    while(lower < upper):
        if (srt_lst[lower] + srt_lst[upper] == target): # equal to target
            return lower, upper
        else: # prepare to increment for new range and try again
            if (srt_lst[lower] + srt_lst[upper] < target): # less than target
                lower += 1
            else: # higher than target
                upper -= 1
    return None


def main():
    #case 1: (1, 3)
    lst1 = [-2, 7, 11, 15, 20, 21]
    tar1 = 22

    print('list: ', lst1)
    print('target: ', tar1)
    print('output should be (1, 3): ', two_sum(lst1, tar1))

    #case 2: None
    tar2 = 100

    print('list: ', lst1)
    print('target: ', tar2)
    print('output should be None: ', two_sum(lst1, tar2))

#main()
