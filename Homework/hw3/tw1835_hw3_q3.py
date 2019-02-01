# rearrange the values by putting them in their corresponding index

def find_duplicates(lst):
    arranged = [0] * len(lst) # create a list of the same size
    duplicates = [0] * len(lst)
    for elem in lst:
        if (arranged[elem] == elem): # if the elem was already put in its matching index before (and therefore is a duplicate)
            duplicates[elem] = elem # then add it to the list of duplicates
        else: # the elem has not been put here yet
            arranged[elem] = elem # then it is the first of its kind and should be put here for reference for future elems

    return [var for var in duplicates if var != 0]

def main():
    lst1 = [2, 4, 4, 1, 2]
    print(find_duplicates(lst1))

    lst2 = [2, 2, 2, 3, 4, 5, 3, 4, 2, 4, 1, 7, 8]
    print(find_duplicates(lst2))

#main()
