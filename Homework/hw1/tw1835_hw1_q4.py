# _____________ a __________________
# return: [1, 10, 100, 1000, 10000, 100000]

[10**var for var in range(0, 6)]

# BELOW: in terms of n, where n is the number of zeros in the last item of the list
# [10**var for var in range(0, n + 1)]


# _____________ b __________________
# return: [0, 2, 6,	12,	20,	30,	42,	56,	72,	90]
#           2  4  6   8   10  12  14  16  18
#    0*2 1*2 2*2 3*2
# 2 * (0 + 1 + 2 + 3 + ... + n)

[2 * sum(range(0, var + 1)) for var in range(0, 9 + 1)] # n + 1 = 10 in this case, n = 9
# BELOW: in terms of n, where n is the number of zeros in the last item of the list
# [2 * sum(range(0, var + 1)) for var in range(0, n + 1)]


# _____________ c __________________
# return [‘a’, ‘b’, ‘c’, ... , ‘z’]

import string
[var for var in string.ascii_lowercase]
