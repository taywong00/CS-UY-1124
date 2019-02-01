class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue_first(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.front_ind = (self.front_ind - 1) % len(self.data)
            self.data[self.front_ind] = elem
            self.num_of_elems += 1

    def enqueue_last(self, elem):
        if(self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.back_ind = (self.back_ind + 1) % len(self.data)
            self.data[self.back_ind] = elem
            self.num_of_elems += 1

    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        elif(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def dequeue_last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.back_ind]
        self.data[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        elif(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.back_ind]

    def resize(self, new_cap):
        old_data = self.data
        new_data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.data = new_data
        self.front_ind = 0
        self.back_ind = self.front_ind + self.num_of_elems - 1
