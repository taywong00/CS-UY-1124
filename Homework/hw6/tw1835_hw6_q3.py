import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str=None):

        self.data = DoublyLinkedList.DoublyLinkedList()
        self.size = 0

        if (orig_str != None):
            curr_count = 0
            for letter in orig_str:
                # if empty or the one before is not same, add new node
                if (self.data.is_empty() or letter != self.data.last_node().data[0]):
                    curr_count = 1
                    new_tuple = (letter, curr_count)
                    self.data.add_last(new_tuple)
                # if letter is the same as in the last node
                else:# add to the tuple of the last node
                    curr_count += 1
                    new_tuple = (letter, curr_count)
                    self.data.delete_last()
                    self.data.add_last(new_tuple)
                self.size += 1


    def __add__(self, other):
        new_str = self.__repr__()
        new_compact_string = CompactString(self.__repr__())
        print('new compact size:', new_compact_string.data.size)
        new_other_string = CompactString(other.__repr__())
        print('new other size:', new_other_string.data.size)

        # end and start letters are the same
        if (new_compact_string.data.last_node().data[0] == new_other_string.data.first_node().data[0]):
            new_count = new_compact_string.data.last_node().data[1] + new_other_string.data.first_node().data[1]
            letter = new_compact_string.data.last_node().data[0]
            new_tuple = (letter, new_count)
            print('new_tuple:', new_tuple)

            # manage first compact string
            new_compact_string.data.add_last(new_tuple) # new last node
            print('new compact\'s last node tuple:', new_compact_string.data.last_node().data)
            print('whole new compact:', new_compact_string.data)
            new_compact_string.data.delete_node(new_compact_string.data.last_node().prev) # delete second to last
            print('whole new compact:', new_compact_string.data)



            # if there are more nodes after the first
            if (new_other_string.data.size > 1):
                print('other size is more than 1')
                new_other_string.delete_first()
                new_compact_string.data.last_node().next = new_other_string.data.first_node()
                new_other_string.data.first_node().prev = new_compact_string.data.last_node()


        else: # end and start letters are different

            new_compact_string.data.last_node().next = new_other_string.data.first_node()
            new_other_string.data.first_node().prev = new_compact_string.data.last_node()
            print('new compact\'s:', new_compact_string)

        return new_compact_string


    def __lt__(self, other):
        num_letters = 0
        self_node = None
        other_node = None

        if (self.size == other.size):
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(self.size):
                #print('self_node.data[0]', self_node.data[0])
                #print('self_node.data[0] is type str', isinstance(self_node.data[0], str))

                if (self_node.data[0] > other_node.data[0]): # self letter > other letter, we greater
                    return False
                elif (self_node.data[1] > other_node.data[1]): # self letter num > other letter num, we greater
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return False # same size, no node differences so far -- same strings

        elif (self.size < other.size):
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(self.size):
                if (self.node.data[0] > other_node.data[0]): # self letter > other letter, we greater
                    return False
                elif (self_node.data[1] > other_node.data[1]): # self letter num > other letter num, we greater
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return True

        else: # self.size > self.other
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(other.size):
                if (other_node.data[0] < self_node.data[0]): # other letter < self letter, we greater
                    return False
                elif (other_node.data[1] < self_node.data[1]): # other letter num < self letter num, we greater
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return False




    def __le__(self, other):
        num_letters = 0
        self_node = None
        other_node = None

        if (self.size <= other.size):
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(self.size):
                if (self.node.data[0] > other_node.data[0]): # self letter > other letter, we greater
                    return False
                elif (self_node.data[1] > other_node.data[1]): # self letter num > other letter num, we greater
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return True

        else: # self.size > self.other
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(other.size):
                if (other_node.data[0] < self_node.data[0]): # other letter < self letter, we greater
                    return False
                elif (other_node.data[1] < self_node.data[1]): # other letter num < self letter num, we greater
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return False

    def __gt__(self, other):
        num_letters = 0
        self_node = None
        other_node = None

        if (self.size == other.size):
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(self.size):
                if (self_node.data[0] < other_node.data[0]): # self letter < other letter, we smaller
                    return False
                elif (self_node.data[1] < other_node.data[1]): # self letter num < other letter num, we smaller
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return False # same size, no node differences so far -- same strings

        elif (self.size > other.size):
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(other.size):
                if (self.node.data[0] < other_node.data[0]): # self letter < other letter, we smaller
                    return False
                elif (self_node.data[1] < other_node.data[1]): # self letter num < other letter num, we smaller
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return True

        else: # self.size < self.other
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(self.size):
                if (other_node.data[0] < self_node.data[0]): # other letter < self letter, we greater
                    return False
                elif (other_node.data[1] < self_node.data[1]): # other letter num < self letter num, we greater
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return False

    def __ge__(self, other):
        num_letters = 0
        self_node = None
        other_node = None

        if (self.size >= other.size):
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(other.size):
                if (self.node.data[0] < other_node.data[0]): # self letter < other letter, we smaller
                    return False
                elif (self_node.data[1] < other_node.data[1]): # self letter num < other letter num, we smaller
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return True

        else: # self.size < self.other
            self_node = self.data.first_node()
            other_node = other.data.first_node()
            for i in range(self.size):
                if (other_node.data[0] < self_node.data[0]): # other letter < self letter, we greater
                    return False
                elif (other_node.data[1] < self_node.data[1]): # other letter num < self letter num, we greater
                    return False
                self_node = self_node.next
                other_node = other_node.next
            return False

    def __repr__(self):
        ret_str = ''
        for node in self.data.__iter__():
            letter_str = node[0] * node[1]
            ret_str += letter_str
        return ret_str

myCS = CompactString('aaaaabbbaaac')
myCS1 = CompactString('aaa')
myCS2 = CompactString('bbb')

print('myCS1:', myCS1)
print('myCS2:', myCS2)

print('myCS1 < myCS2', myCS1 < myCS2)

#myCS3 = myCS1 + myCS2
print(myCS3)







































'''
# print('new_compact_string: ', new_compact_string)
# print('new_compact_string last: ', new_compact_string.data.last_node().data)
for node in new_compact_string.data:
    print(isinstance(node, tuple))

new_other_string = CompactString(other.__repr__())
# print('new_other_string: ', new_other_string)
# print('new_other_string first: ', new_other_string.data.first_node().data)


# assume not empty
# if the end of first = start of second
# if (new_compact_string.data.last_node().data[0] == new_other_string.data.first_node().data[0]):
#     new_count = new_compact_string.data.last_node().data[1] + new_other_string.data.first_node().data[1]
#     new_tuple = (new_compact_string.data.last_node().data[0], new_count)
#
#     # second to last of front --> new_tuple
#     # new_tuple <-- second of back
#     new_compact_string.data.delete_last()
#     new_other_string.data.delete_first()
#     new_compact_string.data.add_last(new_tuple)
#

new_compact_string.data.add_last(new_other_string.data)
# print('new_compact_string.data.last_node().next: ', new_compact_string.data.last_node().next.data)
#new_other_string.data.first_node().prev = new_compact_string.data.last_node()
# print('new_other_string.data.first_node().prev: ', new_other_string.data.first_node().prev.data)
# print(isinstance(new_compact_string, type(None)))
# print(isinstance(new_compact_string.data.first_node(), type(None)))
'''
