import ctypes # provides low-level arrays
def make_array(n):
    return(n * ctypes.py_object)()

class MyList:
    def __init__(self):
        #called automatically on construction time to initialize the data members
        #((FIGURE 1))
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1


    def append(self, val):
        if (self.n == self.capacity): #we cant add val, it would be out of range --> we need to resize
            self.resize(2 * self.capacity)

        self.data[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_data = make_array(new_size) # new array
        for i in range(self.n): # copy data
          new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_size


    # Note: THIS IS A MODIFICATION OF PREVIOUS __getitem__()
    def __getitem__(self, ind):
        if (0 > ind or ind > (self.n - 1)): # index too big or neg
            raise IndexError(str(ind) + " is an out of range index!!!") # in parenthesis: the string you want to print stating your error
        elif (ind < 0): #neg index
            ind = self.n + ind
        return self.data[ind]


    # Note: THIS IS A MODIFICATION OF PREVIOUS __setitem__()
    def __setitem__(self, ind, value):
        if (0 > ind or ind > (self.n - 1)): # index too big or neg
            raise IndexError(str(ind) + " is an out of range index!!!") # in parenthesis: the string you want to print stating your error
        elif (ind < 0): # neg index
            ind = self.n + ind
        self.data[ind] = value


    def __iter__(self): # make generator whereby iter can be called to make an iterable
        for i in range(self.n):
            yield self.data[i]


    def __len__(self):
        return self.n


    def extend(self, other): # simulate what happens in a list: mutates the existing list (not create new one)
        for elem in other:
            self.append(elem) # this is the best implementation, instead of combining size fo self and other, and then doubling the size of a new list based on that--> combined size


    def __repr__(self):
        res = '['
        for i in range(self.n):
            if (i == 0): # if first elem
                res += str(self.data[i])
            else: #every other elem
                res += ', ' + str(self.data[i])
        res += ']'
        return res

        # or
        # return ('[' + ','.join([str(i) for i in self]) + ']')

    def __add__(self, other):
        new_list = MyList()
        new_list.extend(self)
        new_list.extend(other)

        return new_list

        # or
        # lst3 = MyList()
        # lst3 += self
        # lst3 += other
        # return lst3

    def __iadd__(self, other):
        self.extend(other)
        #print(self)
        return self

        # or
        # for i in range(other.n):
        #     self.append(other[i])
        # return self

    def __mul__(self, num):
        new_list = MyList()
        for i in range(num):
            new_list += self
        return new_list

    def __rmul__(self, num):
        return self.__mul__(num)

    # ----------------v-- actual hw3 q2 --v------------------------

    def insert(self, index, val):
        # double the capacity if there is no room for an additional element
        # index error if index (pos or neg) is out of range
        if not(0 <= index <= (self.n - 1)): # index too big or neg
            raise IndexError(str(index) + " is an out of range index!!!") # in parenthesis: the string you want to print stating your error

        if (self.n == self.capacity): #we cant add val, it would be out of range --> we need to resize
            self.resize(2 * self.capacity)

        curr_ind = self.n - 1
        while (curr_ind >= index):
            self.data[curr_ind + 1] = self.data[curr_ind] # shift curr index val 1 spot to the right
            curr_ind -= 1

        self.data[index] = val
        self.n += 1


        

    def pop(self, index=None):
        # raise an index error if the array is empty
        if (self.n == 0):
            raise IndexError(str(index) + " is an out of range index!!!") # in parenthesis: the string you want to print stating your error

        # if no index
        if (index == None):
            # remove the last element
            popped = self.data[self.n - 1] # save last elem in the list

        # given index
        else:
            popped = self.data[index]

            #shift everything to the left to fill in the removed element
            curr_ind = index
            while (curr_ind < self.n - 1): # while not the end
                self.data[curr_ind] = self.data[curr_ind + 1] # set curr index to next val
                curr_ind += 1


        self.data[self.n - 1] = None # replace last elem with None --> "removed"
        self.n -= 1 # last elem is one less index

        # maintain the memory -- when the number of elements is less than 1/4 capacity, halve capacity
        if (self.n < self.capacity // 4):
            self.resize(self.capacity // 2)

        return popped

    # ----------------^-- actual hw3 q2 --^------------------------


#testing
def main():
    mylist1 = MyList()
    for i in range(5):
        mylist1.append(10*(i+1))

    print('mylist1: ' + mylist1.__repr__() + '\n')


    mylist2 = MyList()
    for i in range(5, 10):
        mylist2.append(10*(i+1))

    print('mylist2: ' + mylist2.__repr__() + '\n')



    mylist3 = mylist1 + mylist2
    print('mylist3 = mylist1 + mylist2: ' + mylist3.__repr__() + '\n')



    mylist4 = MyList()
    for i in range(5):
        mylist4.append(i+1)

    print('mylist4: ' + mylist4.__repr__() + '\n')

    mylist4 += mylist2

    print('new mylist4 (after mylist4 += mylist2): ' + mylist4.__repr__() + '\n')

    print('mylist1[0]: ' + str(mylist1[0]) + '\n')

    # print('mylist1[-1]: ' + str(mylist1[-1]) + '\n')

    # mylist1[-2] = 4
    # print('mylist1[-2] = 4: ' + str(mylist1[-2]) + '\n')

    mylist5 = mylist1 * 2
    print('mylist5: ' + mylist5.__repr__() + '\n')

    mylist6 = 2 * mylist1
    print('mylist6: ' + mylist6.__repr__() + '\n')

    mylist6.insert(5, 60)
    print('mylist6, 60 at index 5: ' + mylist6.__repr__() + '\n')

    # mylist6.insert(-2, 60)
    # print('mylist6, 60 at index 5: ' + mylist6.__repr__() + '\n')

    mylist6.pop()
    print('mylist6: ' + mylist6.__repr__() + '\n')

    mylist6.pop()
    print('mylist6: ' + mylist6.__repr__() + '\n')

    mylist6.pop(0)
    print('mylist6 remove ind 0: ' + mylist6.__repr__() + '\n')

    mylist6.pop(1)
    print('mylist6 remove ind 1: ' + mylist6.__repr__() + '\n')

    mylist6.pop(0)
    print('mylist6 remove ind 0: ' + mylist6.__repr__() + '\n')
    mylist6.pop(0)
    print('mylist6 remove ind 0: ' + mylist6.__repr__() + '\n')

#main()
