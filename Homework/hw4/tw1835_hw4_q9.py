def permutations(lst, low, high):
    # given list, int, int
    # return a list of all permutations of the list

    final_permutations =[]

    # base case: 1 elem in the list
    if (high - low == 0):
        final_permutations.append([lst[low]])

    # recursive case: more than one elem in the list
    else:
        existing_permutations = permutations(lst, low, high - 1)
        val = lst[high]

        for each_permutation in existing_permutations:
            # insert the remaining value starting at index 0
            for i in range(0, len(each_permutation) + 1):
                # keep moving it one place to the right for every additional permutation
                curr_permutation = list(each_permutation)
                curr_permutation.insert(i, val)
                final_permutations.append(curr_permutation)

    return final_permutations


print(permutations([1, 2, 3], 0, 2))
