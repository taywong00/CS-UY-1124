# _____________ a __________________
# takes a positive integer n
# returns the sum of the squares < n (pos int only)


def sum_smaller_squares(n):
    curr = 1
    sum = 0

    while (curr < n):
        sum += curr**2
        curr += 1

    return sum



# _____________ b __________________
# single command that produces result of (a)
# using list comp and built-in sum()

# using the example of n = 6:
sum([ var**2 for var in range(1, 6 + 1) if var < 6])

# answer below in terms of n --> n to be replaced by an integer when the command is run:
# sum([ var**2 for var in range(1, n + 1) if var < n])


# _____________ c __________________
# takes positive integer n
# returns the sum of squares of all odd numbers < n

def sum_odd_squares(n):
    curr = 1
    sum = 0

    while (curr < n):
        if curr % 2 == 1 :
            sum += curr**2
        curr += 1

    return sum

# _____________ d __________________
# single command that produces result of (c)
# using list comp and built-in sum()

# using example of n = 6
sum([ var**2 for var in range(1, 6 + 1) if var < 6 and var % 2 == 1])

# answer below in terms of n --> n to be replaced by an integer when the command is run:
# sum([ var**2 for var in range(1, n + 1) if var < n and var % 2 == 1])



def __main__():
    print('\n ___ sum_smaller_squares ___')
    print( '1 + 4 + 9 + 16 + 25 =' , sum_smaller_squares(6) ) #55

    print('\n ___ list comp version ___')
    print(sum([ var**2 for var in range(1, 6 + 1) if var < 6])) #55

    print('\n ___ sum_odd_squares ___')
    print( '1 + 9 + 25 =', sum_odd_squares(6) ) # 35

    print('\n ___ list comp version ___')
    print(sum([ var**2 for var in range(1, 6 + 1) if var < 6 and var % 2 == 1]))

__main__()
