import ArrayStack, ArrayQueue

def permutations(lst):
    stack_num_left = ArrayStack.ArrayStack()
    permutations_queue = ArrayQueue.ArrayQueue()
    num_curr_permutations = 0
    num_new_permutations = 0
    final_permutations_list = []

    # fill the stack with the list elems
    for elem in lst:
        stack_num_left.push(elem)

    # if the perm queue is empty, put the first elem in (only one perm of itself)
    if (num_curr_permutations == 0): # empty queue
        perm = []
        perm.append(stack_num_left.pop())
        permutations_queue.enqueue(perm)
        num_curr_permutations += 1

    # for each remaining num in the stack
    for each_num in range(len(stack_num_left)):
        # for each permutation currently in the queue
        num = stack_num_left.pop()

        for perm in range(num_curr_permutations):
            # insert the curr number at every index starting at 0 to make a new perm
            curr_perm = permutations_queue.dequeue()
            # for every index of this permutation + 1
            for ind in range(len(curr_perm) + 1):
                new_perm = list(curr_perm)
                new_perm.insert(ind, num) # make a new perm with the num inserted at the given index
                permutations_queue.enqueue(new_perm) # add this new perm to the queue
                num_new_permutations += 1
        num_curr_permutations = num_new_permutations


    while (permutations_queue.is_empty() == False):
        final_permutations_list.append(permutations_queue.dequeue())

    return final_permutations_list
