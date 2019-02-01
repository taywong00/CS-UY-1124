def remove_all(lst, value): # [1, 2, 3, 4, 3, 5], 3
    last_ind = len(lst) - 1 # 5
    og_len = len(lst)

    i = 0
    while (i < og_len):
        if (lst[i] != value): # [1, 2, 3, 4, 3, 5, | 1, 2, 4, 5]
            lst.append(lst[i])
        i += 1

    new_len = len(lst) - 1 - last_ind


    i = 0
    for i in range(0, new_len): # [1, 2, 4, 5, | 3, 5, 1, 2, 4, 5 ]
        lst[i] = lst[last_ind + i + 1]
        i += 1

    while (len(lst) != new_len):
        lst.pop()



def main():
    lst1 = [1, 2, 3, 4, 3, 5]
    remove_all(lst1, 3)
    print(lst1)

#main()
