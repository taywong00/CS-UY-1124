def shift(lst, k, going_left = True):

    for each_shift in range(0, k): #repeat shift of 1 for k times

        #shift all elements to the left by 1
        curr_pos = 0 # start at first position
        curr_val = lst[curr_pos] # take value and set it to curr_val
        for elem in lst: #each element needs to be shifted

            #picking direction
            if going_left:
                next_pos = curr_pos - 1
            else: #going right
                next_pos = curr_pos + 1
                if next_pos == len(lst): #would make list out of range
                    next_pos = 0 #wrap back to 0

            next_val = lst[next_pos]    # take value at next_pos and set to next_val
            lst[next_pos] = curr_val  # replace value at next_pos with curr_val
            #modify values for the next iteration
            curr_val = next_val
            curr_pos = next_pos

    return lst


#-------------------------------------------
def __main__():
    print(shift([1, 2, 3, 4, 5, 6], 2, True))
    print(shift([1, 2, 3, 4, 5, 6], 7, False))
    print(shift([1, 2, 3, 4, 5, 6], 2))

#__main__()
