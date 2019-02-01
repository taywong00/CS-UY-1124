def count_lowercase(s, low, high):
    # str, int, int
    # return number of lowercases from low-high

    if (high - low == 0):
        if (s[low].islower()):
            return 1
        else:
            return 0

    else:
        if (s[low].islower()):
            return 1 + count_lowercase(s, low + 1, high)
        else:
            return count_lowercase(s, low + 1, high)


print(count_lowercase('AppleS', 0, 5))



def is_number_of_lowercase_even(s, low, high):
    # given str, int, int
    # return boolean
    # 
    # if (high - low == 0): # considering 1 elem
    #     return False
    #
    # # when calling the funtion on a a smaller range
    # else:
    #     if ()
    #     if ()

    if (count_lowercase(s, low, high) % 2 == 0):
        return True
    else:
        return False



print(is_number_of_lowercase_even('sfw', 1, 2))
