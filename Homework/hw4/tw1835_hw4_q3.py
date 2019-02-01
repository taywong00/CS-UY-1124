def print_triangle(n):
    # given positive int n
    # prints right triangle with asterisks n lines tall

    # base case: n = 1
    if (n == 1):
        print ('*')

    # recursive case:
    # when we call the function on n - 1, it will print a triangle with one less height level
    else:
        print_triangle(n-1)
        print('*' * n)



def print_oposite_triangles(n):
    # given positive int n
    # prints right triangle with asterisks n lines tall AND x-axis reflected triangle

    # base case: n = 1
    if (n == 1):
        print ('*\n*')

    # recursive case:
    # when we call the function on n - 1, it will print
    else:
        print('*' * n)
        print_oposite_triangles(n-1)
        print('*' * n)



def print_ruler(n):
    # given positive int n

    # base case: n = 1
    if (n == 1):
        print('-')

    # recursive case:
    else:
        print_ruler(n-1)
        print('-' * n)
        print_ruler(n-1)



def main():
    print_triangle(4)
    print('\n')
    print_oposite_triangles(4)
    print('\n')
    print_ruler(4)


#main()
