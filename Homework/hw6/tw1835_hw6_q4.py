import DoublyLinkedList

def copy_linked_list(lnk_lst):
    new_lnk_lst = DoublyLinkedList.DoublyLinkedList()

    for big_node in lnk_lst: # for every elem in lnk_lst
        new_lnk_lst.add_last(big_node)

    return new_lnk_lst



def deep_copy_linked_list(lnk_lst):
    new_lnk_lst = DoublyLinkedList.DoublyLinkedList()

    # iterate through the list to copy each elem
    for big_node in lnk_lst:
        new_data = None

        # check if the data member in this node is another list
        # if it is another linked list, make a deep copy of this data
        if (isinstance(big_node, DoublyLinkedList.DoublyLinkedList)):
            new_data = deep_copy_linked_list(big_node)


        # else: make a regualr deep copy of this int
        else:
            new_data = int(big_node)

        # add the new data member (whether DLL or not) to the end of the DLL
        new_lnk_lst.add_last(new_data)

        return new_lnk_lst






def main():
    lnk_lst1 = DoublyLinkedList.DoublyLinkedList()
    elem1 = DoublyLinkedList.DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst1.add_last(elem1)
    elem2 = 3
    lnk_lst1.add_last(elem2)

    lnk_lst2 = deep_copy_linked_list(lnk_lst1)
    print(lnk_lst2)

    e1 = lnk_lst1.first_node()
    e1_1 = e1.data.first_node()
    e1_1.data = 10
    print(lnk_lst1)
    print(lnk_lst2)

    e2 = lnk_lst2.first_node()
    e2_1 = e2.data.first_node()
    print(e2_1.data)

#main()
