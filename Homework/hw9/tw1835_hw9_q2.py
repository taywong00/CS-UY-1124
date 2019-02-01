import ChainingHashTableMap

# worst Time -- UnsortedArrayMap, O(n^2)

def intersection_list(lst1, lst2):
    ret_lst = []
    for num1 in lst1:
        print(num1)
        for num2 in lst2:
            print(num2)
            if (num1 == num2):
                ret_lst.append(num1)

    return ret_lst




# average time -- ChainingHashTableMap
def intersection_list(lst1, lst2):
    hash_map = ChainingHashTableMap.ChainingHashTableMap()
    ret_lst = []
    # put all of one list in the dictionary, check if they exist in that list?
    for key in lst1:
        hash_map[key] = True

    for key in lst2:
        try:
            if (hash_map[key] == True):
                ret_lst.append(key)
        except:
            pass

    return ret_lst





def main():

    lst1 = [3, 9, 2, 7, 1]
    lst2 = [4, 1, 8, 2]
    print(intersection_list(lst1, lst2))

main()
