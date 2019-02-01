from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.top_deque = ArrayDeque()
        self.bottom_stack = ArrayStack()

    def __len__(self):
        return len(self.top_deque) + len(self.bottom_stack)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        if (len(self) % 2 == 1): # even len
            # top deque has one more than bottom stack
            # then shift last deque member to top of stack and enqueue first val to deque
            last_deque = self.top_deque.last()
            self.bottom_stack.push(last_deque)
            self.top_deque.dequeue_last()

        self.top_deque.enqueue_first(e)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.top_deque.first()

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        else:
            if (len(self) % 2 == 0): # top and bottom have same
                # make sure that the top always has one more than the bottom
                top_stack = self.bottom_stack.pop()
                self.top_deque.enqueue_last(top_stack)
            return self.top_deque.dequeue_first()

    def mid_push(self, e):
        if (len(self) % 2 == 0): # top and bottom have same num elem
            self.top_deque.enqueue_last(e)
        else: # top has one more than bottom, make even
            self.bottom_stack.push(e)
