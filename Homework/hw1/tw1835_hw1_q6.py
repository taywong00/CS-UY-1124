import collections

class Vector:
# represent a vector in a multidimensional space

    def __init__(self, d = False, lst = False):
        # create d dimensional vector of 0s
        '''_____ part a _____'''
        #check if iterable
        # try:
            # d_iterator = iter(d)
        # except TypeError as te:
            # print(d, 'is not iterable')


        if isinstance(d, collections.Iterable): #if iterable
            self.coords = [0] * len(d) #make empty list of right length
            for index in range(0, len(d)): #for each index in the vector
                self.coords[index] = d[index] #set the value to the corresponding index in the iterable
        else: #not an iterable -- single integer
            self.coords = [0] * d #just make the empty list of int length


    def __len__(self):
        # Return the dimension of the vector
        return len(self.coords)

    def __getitem__(self, j):
        # Return jth coordinate of vector
        return self.coords[j]

    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value
        self.coords[j] = val

    def __add__(self, other):
        # Return sum of two vectors
        if (len(self) != len(other)): # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of 0s
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result.coords

    def __eq__(self, other):
        # Return True if vector has same coordinates as other
        return self.coords == other.coords

    def __ne__(self, other):
        # Return True if vector differs from other
        return not (self == other)

    def __str__(self):
        # Produce string representation of vector
        return '<' + str(self.coords)[1:1] + '>'

    def __repr__(self):
        #print a representation of x
        #we want to print the objects
        return str(self)

    '''_____ part b _____'''
    def __sub__(self, other):
        # Return sum of two vectors
        if (len(self) != len(other)): # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of 0s
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result.coords

    '''_____ part c _____'''
    def __neg__(self):
        #return a vector with all the values of the negted vector
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = 0 - self[j]
        return result.coords

    '''_____ part d _____'''
    def __mul__(self, other):
        #vector * vector
        if isinstance(other, Vector):
            sum = 0
            #make sure that they are of the same length
            if (len(self) != len(other)): # relies on len method
                raise ValueError("dimensions must agree")
            else: #they are of the same length
                for j in range(len(self)):
                    val = self[j] * other[j]
                    sum += val
            return sum


        else: #vector * other --> other is int
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result.coords

    '''_____ part e _____'''
    def __rmul__(self, num):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * num
        return result.coords



def __main__():
    v = Vector(5)
    print(v.coords)

    v2 = Vector([1, 2, 3])
    print(v2.coords)

    v3 = Vector([1, 2, 3])
    print(v3.coords)

    print('\n v4 = v2 - v3')
    v4 = v2 - v3
    print(v4)

    v5 = -v2
    print(v5)

    v6 = v2*3
    print(v6)

    v7 = 2*v2
    print(v7)

    v8 = v2 * v3
    print(v8)





#__main__()
