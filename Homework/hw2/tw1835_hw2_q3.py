import math

def factors(num):
    # given positive int num
    # returns generator that produces all nums divisors in ascending order
    second_half = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if (num % i == 0): # is a factor
            second_half.append(num // i)
            yield i

    curr = -1
    for each in second_half:
        yield second_half[curr]
        curr -= 1









def __main__():
    #for loop runtime: θ(sqrt(num))
    for curr_factor in factors(100):
        print(curr_factor)

#__main__()
