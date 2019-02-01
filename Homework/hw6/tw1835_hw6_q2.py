import DoublyLinkedList

class Integer:

    def __init__(self, num_str=None):
        self.data = DoublyLinkedList.DoublyLinkedList()

        if (num_str != None):
            for num in num_str:
                self.data.add_last(int(num))

    def __add__(self, other):
        new_integer = Integer()

        num_trav = 0 # number of traversals
        # traverse the smaller number
        if (self.data.size <= other.data.size):
            num_trav = self.data.size
            lower_curr_node = self.data.trailer.prev # start from the last digit
            higher_curr_node = other.data.trailer.prev
        else: # other is the smaller num
            num_trav = other.data.size
            lower_curr_node = other.data.trailer.prev
            higher_curr_node = self.data.trailer.prev

        prev_ten = 0
        for each_node in range(num_trav):
            # add both numbers at the current pos
            new_digit = higher_curr_node.data + lower_curr_node.data + prev_ten
            new_integer.data.add_first(new_digit % 10)
            if (new_digit >= 10):
                prev_ten = 1
            else:
                prev_ten = 0
            higher_curr_node = higher_curr_node.prev
            lower_curr_node = lower_curr_node.prev

        while (higher_curr_node.data != None):
            new_digit = higher_curr_node.data + prev_ten
            new_integer.data.add_first(new_digit % 10)
            if (new_digit >= 10):
                prev_ten = 1
            else:
                prev_ten = 0
            higher_curr_node = higher_curr_node.prev

        return new_integer


    def __repr__(self):
        ret_str = ''
        for node in self.data.__iter__():
            ret_str += str(node)
        return ret_str


def main():

    n1 = Integer('4378')
    n2 = Integer('92')
    print(n1)
    print(n2)

    n3 = n1 + n2 # 4470
    print(n3)



main()
