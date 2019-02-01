import ArrayStack

class Queue:

    def __init__(self):
        self.main_stack = ArrayStack.ArrayStack()
        self.dequeue_stack = ArrayStack.ArrayStack()
        self.first_elem = None

    def __len__(self):
        return len(self.main_stack)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, elem): # from the back
        if (self.is_empty()):
            self.first_elem = elem
        self.main_stack.push(elem)


    def dequeue(self): # from the front
        # transfer all elems of main to dequeue in reverse order to front at top
        for elem in range(len(self.main_stack)):
            self.dequeue_stack.push(self.main_stack.pop())


        # pop off first elem
        popped_val = self.dequeue_stack.top()
        self.dequeue_stack.pop()
        # set new first to curr top after popping
        try:
            self.first_elem = self.dequeue_stack.top()
        except:
            self.first_elem = None
        # put all the elems back into main from dequeue
        for elem in range(len(self.dequeue_stack)):
            self.main_stack.push(self.dequeue_stack.pop())
        # return popped val
        return popped_val


    def first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self.first_elem
