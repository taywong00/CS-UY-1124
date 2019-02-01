import DoublyLinkedList

# runtime O(n1 + n2), n1 = size lst1, n2 = size lst2
def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    #print(srt_lnk_lst1, srt_lnk_lst2)
    # recursive function
    def merge_sublists(srt_sub1_node, srt_sub2_node):
        #print(srt_sub1_node.data, srt_sub2_node.data)
        new_srt_list = DoublyLinkedList.DoublyLinkedList()

        # base case: sublist = last nodes in a sorted list
            # only base case can return something
        # 1: both last nodes
        if (srt_sub1_node is srt_lnk_lst1.last_node() and srt_sub2_node is srt_lnk_lst2.last_node()):
            #print('these nodes are last', srt_sub1_node.data, srt_sub2_node.data)
            # if sub1 <= sub2, add sub1 then sub2
            if (srt_sub1_node.data <= srt_sub2_node.data):
                new_srt_list.add_last(srt_sub1_node.data)
                new_srt_list.add_last(srt_sub2_node.data)
            # else: sub1 > sub2, add sub2 then sub1
            else:
                new_srt_list.add_last(srt_sub2_node.data)
                new_srt_list.add_last(srt_sub1_node.data)

        # 2: if sub1 is last node, sub2 has more
        elif (srt_sub1_node is srt_lnk_lst1.last_node()):
            #print(srt_sub1_node.data, 'is last node but,', srt_sub2_node.data, 'isnt')
            # if sub1 <= sub2, add sub1 then rest sub2
            if (srt_sub1_node.data <= srt_sub2_node.data):
                new_srt_list.add_last(srt_sub1_node.data) # add sub1

                curr_node = srt_sub2_node # add rest sub2
                while (curr_node.data != None):
                    new_srt_list.add_last(curr_node.data)
                    curr_node = curr_node.next

            else: # sub1 > sub2, add sub2 then call merge again with same sub1 node but new sub2 node (sub2.next)
                new_srt_list.add_last(srt_sub2_node.data)
                # new_srt_list.last_node().next = merge_sublists(srt_sub1_node, srt_sub2_node.next).first_node()

                prev = new_srt_list.last_node()
                succ = new_srt_list.last_node().next

                newDLL = merge_sublists(srt_sub1_node, srt_sub2_node.next)

                prev.next = newDLL.first_node()
                succ.prev = newDLL.last_node()

                new_srt_list.size += newDLL.size

        # 3: if sub1 has more, sub2 is last node
        elif (srt_sub2_node is srt_lnk_lst2.last_node()):
            #print(srt_sub2_node.data, 'is last node but,', srt_sub1_node.data, 'isnt')

            # if sub2 <= sub1, add sub2 then rest sub1
            if (srt_sub2_node.data <= srt_sub1_node.data):
                new_srt_list.add_last(srt_sub2_node.data) # add sub2

                curr_node = srt_sub1_node # add rest sub1
                while (curr_node.data != None):
                    new_srt_list.add_last(curr_node.data)
                    curr_node = curr_node.next

            # else: sub2 > sub1, add sub1 then call merge again with same sub2 but new sub1 node (sub1.next)
            else:
                new_srt_list.add_last(srt_sub2_node.data)
                # new_srt_list.last_node().next = merge_sublists(srt_sub1_node.next, srt_sub2_node)

                prev = new_srt_list.last_node()
                succ = new_srt_list.last_node().next

                newDLL = merge_sublists(srt_sub1_node.next, srt_sub2_node)

                prev.next = newDLL.first_node()
                succ.prev = newDLL.last_node()

                new_srt_list.size += newDLL.size

        # 4: if both regular nodes (not last)
        else:
            #print('both are normal nodes', srt_sub1_node.data, srt_sub2_node.data)

            if (srt_sub1_node.data <= srt_sub2_node.data): # sub1 <= sub2
                new_srt_list.add_last(srt_sub1_node.data)
                # new_srt_list.last_node().next = merge_sublists(srt_sub1_node.next, srt_sub2_node)

                prev = new_srt_list.last_node()
                succ = new_srt_list.last_node().next

                newDLL = merge_sublists(srt_sub1_node.next, srt_sub2_node)

                prev.next = newDLL.first_node()
                succ.prev = newDLL.last_node()

                new_srt_list.size += newDLL.size

                #print('curr new DLL', newDLL)


            else: # sub1 > sub2
                new_srt_list.add_last(srt_sub2_node.data)
                # new_srt_list.last_node().next = merge_sublists(srt_sub1_node, srt_sub2_node.next)

                prev = new_srt_list.last_node()
                succ = new_srt_list.last_node().next

                newDLL = merge_sublists(srt_sub1_node, srt_sub2_node.next)

                prev.next = newDLL.first_node()
                succ.prev = newDLL.last_node()

                new_srt_list.size += newDLL.size

        #print('new_srt_list after checking ', srt_sub1_node.data, srt_sub2_node.data)
        #print(new_srt_list)
        return new_srt_list



    return merge_sublists(srt_lnk_lst1.first_node(), srt_lnk_lst2.first_node())



def main():

    lst1 = DoublyLinkedList.DoublyLinkedList()
    lst1_elems = [1, 3, 5, 6, 8]
    for item in lst1_elems:
        lst1.add_last(item)
    print(lst1)

    lst2 = DoublyLinkedList.DoublyLinkedList()
    lst2_elems = [2, 3, 5, 10, 15, 18]
    for item in lst2_elems:
        lst2.add_last(item)
    print(lst2)

    merged_lst = merge_linked_lists(lst1, lst2)
    print(merged_lst)

#main()



        #
        # if (srt_sub1_node is srt_lnk_lst1.trailer and srt_sub2_node is srt_lnk_lst2.trailer):
        #     return
        # elif (srt_sub1_node is srt_lnk_lst1.trailer): # end of 1
        #     return # something
        # elif (srt_sub2_node is srt_lnk_lst2.trailer): # end of 2
        #     return # something
        # else: # two integers
        #     if (srt_sub1_node.data <= srt_sub2_node.data): # sub1 <= sub2
        #         new_srt_list.add_last(srt_sub1_node)
        #         return merge_sublists(srt_sub1_node.next, srt_sub2_node, new_srt_list)
        #     else: # sub1 > sub2
        #         new_srt_list.add_last(srt_sub2_node)
        #         return merge_sublists(srt_sub1_node, srt_sub2_node.next, new_srt_list)

        # base case: sublist = last nodes in a sorted list


        # if (srt_sub1_node is not srt_lnk_lst1.trailer and srt_sub2_node is not srt_lnk_lst2.trailer):
        #     if (srt_sub1_node <= srt_sub2_node): # 1 <= 2
        #         new_srt_list.add_last(srt_sub1_node.data)
        #         return
        #     else:
        #         new_srt_list.add_last(srt_sub2_node.data)
        #
        #
        # return merge_sublists(srt_sub1_node.next, srt_sub2_node.next, new_srt_list)
        #
        #




'''


'''
