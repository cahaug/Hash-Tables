# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.length = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # take the key and value, and put it somewhere in the array
        # get an index for the key
        index = self._hash_mod(key)
        # link_pair = LinkedPair(key, value)
        # if storage is not empty at the index, handle the collison
        if self.storage[index] is not None:
            # print('Warning: Collision detected for key ' + key)
            # create a new node
            newNode = LinkedPair(key,value)
            # set the prev node to the next node of our new node
            newNode.next = self.storage[index]
            #set the new node as the head
            self.storage[index] = newNode
        # if storage is empty
        else:
            self.storage[index] = LinkedPair(key, value)
            


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # check if the index is empty
        if self.storage[index] is not None:
            # check if the index has been collided with, if so, traverse the list looking for the key. print error if not
            if self.storage[index].next is not None:
                currentNode = self.storage[index]
                prevNode = None
                keyRemoved = False
                while currentNode is not None:
                    if key == currentNode.key:
                        #remove the node
                        if prevNode is None:
                            #we are at the head of a list, set the next node to the head
                            keyRemoved = True
                            self.storage[index] = currentNode.next
                        else:
                            #we are in a list, set currentNode.next to the previous node
                            keyRemoved = True
                            prevNode.next = currentNode.next
                    #key was not found, advance to the next node
                    prevNode = currentNode
                    currentNode = currentNode.next
                # if we ran the list at the index and couldn't find the key to remove, warn the user
                if keyRemoved == False:
                    print("WARNING: Could not Remove at Index " + str(index))
            else:
                #or, it was the only key at the index, so remove it
                self.storage[index] = None
        else:
            print("WARNING: The index is empty")



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # return empty if empty
        if self.storage[index] is None:
            return None
        else:
            # check if the index has been collided with
            if self.storage[index].next is not None:
                currentNode = self.storage[index]
                # look through the list
                while currentNode is not None:
                    if key == currentNode.key:
                        # if key, return value
                        return currentNode.value
                    # if not, advance to next node
                    currentNode = currentNode.next
            else:
                return self.storage[index].value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        # create a new array size * 2
        self.storage = [None] * self.capacity
        # move all values over
        for pair in old_storage:
            # figure out the new correct place for the key/value
            # new_index = self._hash_mod(pair.key)
            # reinsert the value
            # OR
            # re-insert each key / value

            # if our pair has a value
            if pair is not None:
                # and is an uncollided index
                if pair.next is None:
                    self.insert(pair.key,pair.value)
                else:
                    # traverse the singly linked list of our LinkedPairs, inserting as we go
                    collidedIndexPair = pair
                    while collidedIndexPair is not None:
                        self.insert(collidedIndexPair.key,collidedIndexPair.value)
                        collidedIndexPair = collidedIndexPair.next

        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
