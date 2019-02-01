import ChainingHashTableMap
import string


# use loser( to lowercase cast)

class InvertedFile:
    def __init__(self, file_name):
        ''' Initializes an InvertedFile object representing
        the inverted file of file_name'''

        with open(file_name, 'r') as myfile:
            D = myfile.read() # turn text file into string

        D = D.lower() # turn all letters lowecase
        D = D.split() # turn long string into a list

        D = [''.join(c for c in s if c not in string.punctuation) for s in D] # remove punctuation
        # print(D)

        self.file_map = ChainingHashTableMap.ChainingHashTableMap()

        for ind in range(len(D)):
            word = D[ind]
            try:
                list_curr_inds = self.file_map[word]
                list_curr_inds.append(ind)
            except:
                list_curr_inds = [ind]

            self.file_map[word] = list_curr_inds


        # ChainingHashTableMap.print_hash_table(self.file_map)



    def indices(self, word):
        ''' Returns a list containing all the indices of
        the places in the file where word appears '''
        try:
            return self.file_map[word]
        except:
            return []

def main():

    inv_file = InvertedFile('row_your_boat.txt') # has 39 words
    print(inv_file.indices("row"))
    print(inv_file.indices("the"))
    print(inv_file.indices("done"))

# main()
