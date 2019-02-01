import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList.DoublyLinkedList()
        self.num_of_elems = self.data.size

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        self.data.add_last(elem)

    def dequeue(self):
        return self.data.delete_first()

    def first(self):
        return self.data.header.next.data

    # do we need a resize function?
    # def resize(self, new_cap):

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self.data.__iter__()]) + "]"

def main():

    myLQ = LinkedQueue()
    print(myLQ)

    myLQ.enqueue(1)
    myLQ.enqueue(2)
    myLQ.enqueue(3)
    myLQ.enqueue(4)
    print(myLQ)

    myLQ.dequeue()
    print(myLQ)

    print(myLQ.first())

    myLQ.dequeue()
    print(myLQ)

    print(myLQ.first())

#main()
