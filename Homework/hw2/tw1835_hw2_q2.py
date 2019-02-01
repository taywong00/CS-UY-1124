def example1(lst): # n^2
    ””” Return the sum of the prefix sums of sequence S.”””
    n = len(lst) # 1
    total = 0 # 1
    for j in range(n): # n
        for k in range(1+j): # n
            total += lst[k] # 1
    return total # 1

def example2(lst) : # n
    ”””Return the sum of the prefix sums of sequence S.”””
    n = len(lst) #1
    prefix = 0 #1
    total = 0 #1
    for j in range(n): # n
        prefix += lst[j] # 1
        total += prefix # 1
    return total  # 1

def example3(n): # 2log(n)
     i = 1 # 1
     sum = 0 # 1
     while (i < n*n): # n^2 # first time is 1, 2, 4, 8, 16 --> so the range starts at n^2
         i *= 2 # but each iteration since i is doubling, the range is halfing each iteration so log (base 2) (n^2) = 2log(n)
         sum += i
     return sum # 1

def example4(n): # n
    i = n
    sum = 0
    while (i > 1): # bc (as below) i is getting infinitely smaller, i cant get any bigger then 2 (but less than)
        for j in range(i): # n times, but getting infinitely smaller (n, n/2, n/4)
            sum += i*j # 1
         i //= 2 # 1, divide i by 2
    return sum
