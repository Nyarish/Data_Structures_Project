
class DoubleNode():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
            
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
    def print_linked_list(self):
        output = list()
        current_node = self.head
        
        while current_node is not None:
            output.append(current_node.value)
            current_node = current_node.next 
            
        print(output)

        
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache_array = [None for _ in range(capacity)]
        self.capacity = capacity
        self.key_list = DoublyLinkedList()
        self.num_entries = 0


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        key = key -1
        if key > self.num_entries:
            return -1
        elif self.cache_array[key] is not None:
            new_head = self.key_list.head
            self.key_list.head = self.key_list.head.next
            self.key_list.tail.next = new_head
            self.key_list.tail = self.key_list.tail.next
            return self.cache_array[key]
        else:
            return -1
            

    def set(self, key, value):
        # Set the value if the key is not present in the cache. 
        # If the cache is at capacity remove the oldest item. 
        if self.capacity == 0:
            print("The cache has Zero capacity")
            return None
        
        key = key -1
        if key >= self.capacity:
            
            key = key % self.capacity 
        if self.cache_array[key] is None:
            self.cache_array[key] = value
            self.num_entries += 1
            
            if self.key_list is None:
                self.key_list.head = DoubleNode(key)
                self.key_list.tail = self.key_list.head
            else:
                self.key_list.append(key)
        else:
            if self.num_entries == self.capacity:
                key_to_remove = self.key_list.head.value
                self.cache_array[key_to_remove] = None
                
                self.num_entries -= 1
                
            else:
                print("That Key is filled")
                
        print("Current Fill level is now at {}".format(self.num_entries))
print("__________________________________________________________________")
# Test case 1
print("Test case 1 LRU_Cache(5)")
print("__________________________________________________________________")

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print()
print("This value {} is in the cache".format(our_cache.get(1)))      # returns 1
print("This value {} is in the cache".format(our_cache.get(2)))      # returns 2
print("This value {} is in the cache".format(our_cache.get(9)))      # returns -1 because 9 is not present in the cache

print()
our_cache.set(5, 5) 
our_cache.set(6, 6)

print()
print("This value {} is in the cache".format(our_cache.get(3)))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("__________________________________________________________________")
# Test case 2
print("Test case 2 LRU_Cache(3)")
print("__________________________________________________________________")

our_cache = LRU_Cache(3)

our_cache.set(1, 1);
our_cache.set(3, 3);
our_cache.set(4, 4);

print()
print("This value {} is in the cache".format(our_cache.get(1)))      # returns 1
print("This value {} is in the cache".format(our_cache.get(2)))      # returns 2
print("This value {} is in the cache".format(our_cache.get(9)))      # returns -1 because 9 is not present in the cache

print()
our_cache.set(5, 5) 
our_cache.set(6, 6)

print()
print("This value {} is in the cache".format(our_cache.get(3)))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("__________________________________________________________________")
# Test case 3
print("Test case 3 LRU_Cache(1)")
print("__________________________________________________________________")

our_cache = LRU_Cache(1)

our_cache.set(3, 3);
our_cache.set(4, 4);

print()
print("This value {} is in the cache".format(our_cache.get(1)))      # returns 1
print("This value {} is in the cache".format(our_cache.get(2)))      # returns 2
print("This value {} is in the cache".format(our_cache.get(9)))      # returns -1 because 9 is not present in the cache

print()
our_cache.set(5, 5) 
our_cache.set(6, 6)

print()
print("This value {} is in the cache".format(our_cache.get(3)))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("__________________________________________________________________")
# Test case 4
print("Test case 4 with LRU_Cache(0)")
print("__________________________________________________________________")

our_cache = LRU_Cache(0)

our_cache.set(3, 3);
our_cache.set(4, 4);

print()
print("This value {} is in the cache".format(our_cache.get(3)))      # returns 1
print("This value {} is in the cache".format(our_cache.get(4)))      # returns 2
# print("This value {} is in the cache".format(our_cache.get(9)))      # returns -1 because 9 is not present in the cache

print()
our_cache.set(5, 5) 
our_cache.set(6, 6)

print()
print("This value {} is in the cache".format(our_cache.get(3)))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry



"""OUTPUT
__________________________________________________________________
Test case 1 LRU_Cache(5)
__________________________________________________________________
Current Fill level is now at 1
Current Fill level is now at 2
Current Fill level is now at 3
Current Fill level is now at 4

This value 1 is in the cache
This value 2 is in the cache
This value -1 is in the cache

Current Fill level is now at 5
Current Fill level is now at 4

This value -1 is in the cache
__________________________________________________________________
Test case 2 LRU_Cache(3)
__________________________________________________________________
Current Fill level is now at 1
Current Fill level is now at 2
That Key is filled
Current Fill level is now at 2

This value 1 is in the cache
This value -1 is in the cache
This value -1 is in the cache

Current Fill level is now at 3
Current Fill level is now at 2

This value -1 is in the cache
__________________________________________________________________
Test case 3 LRU_Cache(1)
__________________________________________________________________
Current Fill level is now at 1
Current Fill level is now at 0

This value -1 is in the cache
This value -1 is in the cache
This value -1 is in the cache

Current Fill level is now at 1
Current Fill level is now at 0

This value -1 is in the cache
__________________________________________________________________
Test case 4 with LRU_Cache(0)
__________________________________________________________________
The cache has Zero capacity
The cache has Zero capacity

This value -1 is in the cache
This value -1 is in the cache

The cache has Zero capacity
The cache has Zero capacity

This value -1 is in the cache
"""