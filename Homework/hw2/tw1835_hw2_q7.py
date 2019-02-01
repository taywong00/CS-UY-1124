def findChange(lst01):
    # lst01 is list of 0s then 1s
    # returns index of first 1
    # runtime: log(n)
    lower = 0
    upper = len(lst01) - 1
    recent1 = None
    while (lower < upper):
        mid = (lower + upper) // 2
        if (lst01[mid] == 0):
            lower = mid + 1
        else: # if mid val is a 1
            recent1 = mid
            upper = mid - 1

    return recent1


def main():

    lst = [0, 0, 0, 0, 0, 1, 1, 1]
    print(lst)
    print('should be 5: ', findChange(lst))

    lst2 = [0, 0, 0, 0, 0]
    print(lst2)
    print('should be None: ', findChange(lst2))

#main()
