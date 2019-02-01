import random
import UnsortedArrayMap as unsorted_map
import DoublyLinkedList

class ChainingHashTableMap:

    def __init__(self, N=64, p=40206835204840513073):
        self.N = N
        self.iter_DLL = DoublyLinkedList.DoublyLinkedList()
        self.table = [unsorted_map.UnsortedArrayMap() for i in range(self.N)]
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        return curr_bucket[key].data.value # added .data.value to get the actual value

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        new_item = unsorted_map.UnsortedArrayMap.Item(key, value)

        # if UnsortedArrayMap is empty/DLL empty
        if (self.iter_DLL.is_empty()):
            new_node = self.iter_DLL.add_first(new_item) # updating DLL
            # adding to the UnsortedArrayMap
            curr_bucket[key] = new_node
            self.n += 1

        else:
            # check if they key exists
            # if the key exists, then change the value
            try:
                curr_bucket[key].data.value = value

            except: # else (the key does not exist), the create a new node
                 new_node = self.iter_DLL.add_last(new_item)
                 curr_bucket[key] = new_node
                 self.n += 1


        if (self.n > self.N):
            self.rehash(2 * self.N)



    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]

        # delete from the DLL
        self.iter_DLL.delete_node(curr_bucket[key])

        # delete from the UnsortedArrayMap
        del curr_bucket[key]
        self.n -= 1
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)



    def __iter__(self):
        for item in self.iter_DLL:
            yield item.key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val


def main():

    ht = ChainingHashTableMap()
    ht['row'] = 3
    ht['hello'] = 1
    ht['world'] = 100000
    ht['the'] = 78

    print(ht['row'])

    for item in ht:
        print(item)


# main()
