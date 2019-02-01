def appearances(s, low, high):
    # given str, int, int
    # return a dictionary of key value pairs, letter: num times it shows up in str

    # base case: only looking at 1 char
    if (high - low == 0):
        dict = {}
        dict[s[low]] = 1
        return dict

    else:
        # dict on a smaller range (low + 1, high)
        dict = appearances(s, low + 1, high)
        if (s[low] in dict):
            dict[s[low]] += 1
        else:
            dict[s[low]] = 1

        return dict

print(appearances('Hello world', 0, 10))
