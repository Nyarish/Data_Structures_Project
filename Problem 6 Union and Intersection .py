
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    
    # intilize the LinkedList()
    unions = LinkedList()
    
    # create a set to hold unique values
    batch_1 = set()
    batch_2 = set()
    
    # check if lits have values
    if llist_1.head is None and llist_2.head is None:
        return None
    
    current_batch_1 = llist_1.head
    while current_batch_1 is not None:
        batch_1.add(current_batch_1.value)
        current_batch_1 = current_batch_1.next
    
    current_batch_2 = llist_2.head
    while current_batch_2 is not None:
        batch_2.add(current_batch_2.value)
        current_batch_2 = current_batch_2.next
    # use recursion
    combined_batch_set = batch_1.union(batch_2)
    
    for batch in combined_batch_set:
        unions.append(batch)
    
    return unions

def intersection(llist_1, llist_2):
    # intilize the LinkedList()
    intersection = LinkedList()
    
    # create a set to hold unique values
    batch_1 = set()
    batch_2 = set()
    
    # check if lits have values
    if llist_1.head is None and llist_2.head is None:
        return None
    
    current_batch_1 = llist_1.head
    while current_batch_1 is not None:
        batch_1.add(current_batch_1.value)
        current_batch_1 = current_batch_1.next
    
    current_batch_2 = llist_2.head
    while current_batch_2 is not None:
        batch_2.add(current_batch_2.value)
        current_batch_2 = current_batch_2.next
    
    # use recursion
    combined_batch_set = batch_1.intersection(batch_2)
    
    if len(combined_batch_set) == 0:
        return None
    for batch in combined_batch_set:
        intersection.append(batch)
        
    return intersection


# Test case 1
print('Test case 1')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("The union of the two list is:\n",union(linked_list_1,linked_list_2))
print ("The intersection of the two list is:\n",intersection(linked_list_1,linked_list_2))

print()
# # Test case 2
print('Test case 2')
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("The union of the two list is:\n",union(linked_list_3,linked_list_4))
print ("The intersection of the two list is:\n",intersection(linked_list_3,linked_list_4))

print()
# # Test case 3
print('Test case 3')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_4.append(i)

for i in element_2:
    linked_list_5.append(i)

print ("The union of the two list is:\n",union(linked_list_5,linked_list_6))
print ("The intersection of the two list is:\n",intersection(linked_list_5,linked_list_6))


"""OUTPUT

Test case 1
The union of the two list is:
 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
The intersection of the two list is:
 4 -> 21 -> 6 -> 

Test case 2
The union of the two list is:
 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
The intersection of the two list is:
 None

Test case 3
The union of the two list is:
 1 -> 21 -> 7 -> 8 -> 9 -> 11 -> 
The intersection of the two list is:
 None

"""





