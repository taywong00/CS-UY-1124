from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.curr_max = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        # check who is the current max at the time
        if (self.is_empty()):
            self.data.push(tuple((e, e))) # val, currmax (its won max bc nothing else)
            self.curr_max = e
        else:
            if (e > self.curr_max):
                self.curr_max = e
            self.data.push(tuple((e, self.curr_max)))

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.top()[0]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        popped_val = self.top()
        self.data.pop()
        self.curr_max = self.data.top()[1] # next max to max down
        return popped_val

    def max(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.curr_max


# maxS = MaxStack()
# maxS.push(3)
# maxS.push(1)
# maxS.push(6)
# maxS.push(4)
# print(maxS.max())
# print(maxS.pop())
# print(maxS.pop())
# print(maxS.max())
