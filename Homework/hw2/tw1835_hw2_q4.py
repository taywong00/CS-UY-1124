def e_approx(n):
    # given a positive int n
    # returns an approximation of e
    #   based on the sum of the first n + 1 addends of the infinite sum
    # RUNTIME: n
    e = 1
    prev_fact = 1
    for i in range(1, n + 1):
        e += 1 / (prev_fact * i)
        prev_fact = prev_fact * i
    return e


# testing
def main():

     for n in range(15):
         curr_approx = e_approx(n)
         approx_str = "{:.15f}".format(curr_approx)
         print("n =", n, "Approximation:", approx_str)

#main()
