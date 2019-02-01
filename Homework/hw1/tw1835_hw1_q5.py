# given	a positive integer n
# returns a generator when iterated over will have the first n elements in the fibonacci seq

def fibs(n):
    prev2 = 0
    prev1 = 1
    counter = 0
    while counter < n:

        if counter < 1:
            yield 1
            counter += 1

        else:
            new = prev2 + prev1
            yield new
            prev2 = prev1
            prev1 = new
            counter += 1


def __main__():
    #test
    for curr in fibs(8):
        print(curr)

    #1 1 2 3 5 8 13 21

#__main__()
