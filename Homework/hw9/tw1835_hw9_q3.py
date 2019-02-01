import random
import UnsortedArrayMap as unsorted_map

class ChainingHashTableMap:

    def __init__(self, N=64, p=40206835204840513073):
        self.N = N

        # self.table = [unsorted_map.UnsortedArrayMap() for i in range(self.N)]
        self.table = [None for i in range(self.N)]

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

        if (isinstance(curr_bucket, unsorted_map.UnsortedArrayMap)): # is a unsorted array map
            return curr_bucket[key]
        else: # has the ditrect item
            return curr_bucket.value


    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]

        if (isinstance(curr_bucket, unsorted_map.UnsortedArrayMap)): # is already an unsorted array map, just add another value to the UnsortedArrayMap
            old_size = len(curr_bucket)
            curr_bucket[key] = value
            new_size = len(curr_bucket)

            if (new_size > old_size):
                self.n += 1

        else: # directly contains the item, curr_bucket = item

            if (curr_bucket == None): # if bucket has None, add item
                self.table[i] = unsorted_map.UnsortedArrayMap.Item(key, value)
                self.n += 1
            elif (key == curr_bucket.key): # if bucket has item with same key, change value
                curr_bucket.value = value
            else: # if bucket has item with different key, make this bucket into an UnsortedArrayMap with both items
                existing_item = curr_bucket
                self.table[i] = unsorted_map.UnsortedArrayMap()
                self.table[i][existing_item.key] = existing_item.value #insert existing item
                self.table[i][key] = value # insert new item
                self.n += 1

        if (self.n > self.N):
            self.rehash(2 * self.N)



    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]

        if (curr_bucket == None):
            raise Exception(key, 'is not a valid key.')

        elif (isinstance(curr_bucket, unsorted_map.UnsortedArrayMap)): # is already an unsorted array map, delete value in the unsorted map
            del curr_bucket[key]
            # if the UnsortedArrayMap is size 1, turn back to single value
            if (len(curr_bucket) == 1):
                self.table[i] == curr_bucket.table[0]

        # note: dont have to worry about if bucket is None, should never happen because it it would need a key

        else: # bucket  with single item exists
            self.table[i] = None

        self.n -= 1

        if (self.n < self.N // 4):
            self.rehash(self.N // 2)



    def __iter__(self):
        for curr_bucket in self.table:
            if (isinstance(curr_bucket, unsorted_map.UnsortedArrayMap)):
                for key in curr_bucket:
                    yield key
            elif (curr_bucket != None):
                yield curr_bucket.key



    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val

def print_hash_table(ht):
    for i in range(ht.N):
        print(i, ": ", sep="", end="")
        curr_bucket = ht.table[i]
        if (isinstance(curr_bucket, unsorted_map.UnsortedArrayMap)):
            for key in curr_bucket:
                print("(", "key:", key, ", ", "value:",curr_bucket[key], ")", sep="", end="")
            print()
        elif (isinstance(curr_bucket, unsorted_map.UnsortedArrayMap.Item)):
            print("(", "key:",curr_bucket.key, ", ", "value:", curr_bucket.value, ")", sep="", end="")
            print("item")
        else:
            print("yur")


# ht = ChainingHashTableMap()
# for i in range(20):
#     ht[i] = i * i
#
# for i in range(20):
#     if (i % 2 == 0):
#         del ht[i]
#
# print_hash_table(ht)
