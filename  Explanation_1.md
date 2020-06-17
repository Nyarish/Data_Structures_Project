##### Explanation_1: LRU Cache


#### Requirement:

An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, i am consider both the `get` and `set` operations as an use operation. The lookup operation (i.e., `get()`) and put() / `set()` is supposed to be fast for a cache memory.

**Note:** Theoretically, the worst case time complexity of `put` and `get` operations of a HashMap can be $O(\dfrac{n}{b}) \approx O(n)$, when $b < < n$ . However, our hashing functions are sophisticated enough that in real-life we easily avoid collisions and never hit `O(n)`. Rather, for the most part, we can safely assume that the time complexity of `put` and `get` operations will be `O(1)`. 

#### Solution to problem:

The approcah i took is to use the below two data sctucture to optimise the time complexity and space complexity.
1. `DoublyLinked` list : Is able to append to the tail in constant time.
2. `Hashtable`: Offers a constant lookup time

#### Time Complexity
Thus by using the two data sctucture `DoublyLinked list` and `Hashtable`, together with the `get()` and `set()`. The `Time Complexity` of this approach is O(1)

#### Space complexity
The `Space complexity` is that of `input space` for `DoublyLinked` is O(n), `Hashtable`is O(n), and that of `Auxillary Space`. Thus the sum of Input Size + Auxillary Space is `=> O(n + 1) => O(n)`




##### Explanation_2 : File Recursion

[//]: # (Image References)


[image1]: image4.png "Encoded text function"


#### Requirement:

For this problem, the goal is to write code for finding all files under a directory `testdir` (and all directories beneath it) that end with ".c"

#### Solution to problem:

The approcah i took is to implement the solution is to use a `find_files(suffix, path)` which takes `suffix (file extension)` and `path (directory path where we need to search)`.I then recursively searched for a file with a given extension in a parent directory and all its sub-directories. I then store all these files with a given suffix in a list and then returning it.

![alt text][image4]

#### Time Complexity

The `Time Complexity` of the function above is `O(n)`. 
This is becuase of the three for loops, `recursive step`, and  `listdir(path) ` is => O(n)

#### Space complexity

The `Space complexity` is that of `input space` for `suffix (str) - O(1)`, `path (str) - O(1)`, and that of `recursive` that is `depth iterations => O(depth * Average number of directories in each level)`


Thus the sum of `Input Size + Auxillary Space is ` which is `=> O(depth * Average number of directories in each level + depth)` and, `=> O(depth * Average number of directories in each level)`


##### Explanation_3 Huffman Coding

[//]: # (Image References)


[image1]: image1.png "Encoded text function"
[image2]: image2.png "Huffman_encoding"
[image3]: image3.png "Huffman decoding"


#### Requirement:

The `Huffman Coding` is a `lossless` data compression algorithm. A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information.A detailed explanantion of the Huffman can be found [here](https://medium.com/iecse-hashtag/huffman-coding-compression-basics-in-python-6653cdb4c476) and the [Udacity's](https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0/modules/a5f68248-862f-4a72-8682-24b86e2f6d61/lessons/a640374a-90af-40ad-85ff-1c6ce3948219/concepts/b97f3d67-ed9e-4759-8841-d13096f5cdd7) Problem 3: Huffman Coding, Overview on Data Compression which is detailed for this problem. 


#### Solution to problem: Code design

The concept behind Huffman Coding is that there has to be fewer bits assigned for frequently occurring letters and more bits for less frequent ones. Here is the approach i took for this problem. 

`huffnam_encoding`:

First, for a given string I will find the frequency of each character and store it in a dictionary.
I will then construct a heap using Python's heapq module.
We build a Huffman Tree using the constructed heap where we will join two lowest value nodes until we have a root node.
We then add 0 all left branches and 1 to all right branches.
We encode the given text based on these values and send encoded_text and heaptree to huffman_decode function.



##### Time Complexity

`Encoding`: `O(n^2)` for:

Finding the frequency of each charachter is `O(n)` (loop once through the input)
from building the tree and since i'm storing the nodes in a dictionary, then it takes in the worst case 2 loops through the dictionary to find the 2 nodes with the lowest weight, in the dectionary to replace 2 nodes with 1 `O(n)`, and we need to repeat this until we have 1 node left `O(n-1)` this gives us `O(n^2-n`).

`generating the code: O(nlogn)` where in the the number of unique charachters in the data (the number of leafes in the tree)
replacing the charachters in the string (encode), takes `O(n^2)` because here we are replacing charachters in the string.

`Decoding: also O(n^2)`

`generating the reverse code: O(nlogn)` where in the the number of unique charachters in the data (the number of leafes in the tree)
`O(n^2) `where n is the length of the encoded data for building the string, loops over all charachters in the encoded data, and for each match with the reverse_code dictionary, it bulds a new string` O(n)`


#### Space Complexity

`O(u*log(u))` from the tree for encoding
`decoding O(n)` where n is the length of the string.


##### Explanation_4 : Active Directory


#### Requirement:

Write a function that provides an efficient look up of whether the user is in a group.

#### Solution to problem: Code design 

The approcah i took is to implement the solution is to use a `Group class` which will perform all the group related operations such as `add_group`, `add_user`, `get_groups`, `get_users`, and `get_name`.

In order to check if a user exists in a particular group or in group's groups (subgroups), I have used a function `is_user_in_group` which takes `user` and `group` as parameters.

First, the function `is_user_in_group` will check if a user exists in a given group. If he exists then it returns True.
If not, it will check for all the subgroups of a given group recursively and return True if he exists in any of the subgroups. Return False otherwise.

#### Time Complexity

`users is a list of users`. To check if a user exists in this list is a linear operation. If `n` is the length of this users list `=> O(n)`


`group_list` is a list of groups at each level. Iteating through this list is also `linear => O(n)`. If there are k number of groups (branches) in each level in depth, then the total number of groups is braches^depth. Let us call this n.

For `recursion`, time complexity for a tree of n nodes (here groups) is `O(n)` and for each node there is a list of `users of length l` and `list of groups of length g` that we need to search for a user. So the time complexity `is O(n* (l+g))`

#### Space Complexity

Input Space:

`users => O(l)`
`group_list => O(g)`

Input space for `one iteration => O(g+l)`
Input space for `depth iteration => O( depth * (g+l) )`

Auxiliary Space:

The recursive function is exhausted only if it has traversed every directory. In other words, when it has reached the depth. Therefore O(depth) space is required in the call stack.
`Total Space Complexity = Input Space + Auxiliary Space => O(depth*(g+l)) + O(depth) => O(depth*(g+l))`




##### Explanation_5 : Blockchain


#### Requirement:

A [Blockchain](https://en.wikipedia.org/wiki/Blockchain) is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash, the [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.



#### Solution to problem: Code design 

The approcah i took is to implement the solution is to use two classes namely `Block` and `BlockChain`. Block class is a template of a `LinkedList node` and BlockChain class is used to `implement a LinkedList`. Inside the BlockChain class, I have three functions namely `append()`, `size()` and `to_list()` which will append nodes to the end of a LinkedList, return its length and return a list of nodes respectively.



#### Time Complexity

`append()` takes `O(1`) since we are adding a new node at the head.

`size()` takes `O(n)` since we have to traverse the entire LinkedList to find the length of a LinkedList

`to_list()` also takes `O(n)` as we have to traverse the entire LinkedList to copy each node's value to this list.

`Total: O(1 + n + n) => O(n)`

#### Space Complexity

Space complexity is `O(n)` as we need a constant space to store each node. Therefore for n nodes, space complexity grows linearly.


##### Explanation_6 :  Union and Intersection 


#### Requirement:

Take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.

#### Solution to problem: Code design 

The approcah i took is to implement the solution is, in the given two linked lists, I have put their values in two `sets` respectively. For finding Union and Intersection, I have used Python's built-in union and intersection operations on a set. This will give the desired union and intersection outputs. Based on these values, I am creating a new LinkedList called Unions and Intersections and returning them respectively.

#### Time Complexity

All methods in the LinkedList class such as `append()`, `size()`, `__str__ `take `linear time complexity i.e, O(n) and O(m) respectively`. Let `n` be the length of LinkedList-1 and `m` be the lengh of LinkedList-2.

In the worst case, elements of both LinkedLists could be `unique for union function => O(n + m)`

In the worst case, elements of both LinkedLists could be similar for `intersection function => O(n) where n=m`.

##### Space Complexity

In the worst case, elements of both LinkedLists could be unique for `union function => O(n + m)`

In the worst case, elements of both LinkedLists could be similar for `intersection function => O(n)`


##### Acknowledgement

I want to acknowledge the help i got for this entire project, from the mentors at Udacity, the knowledge forum and chats on the student portal. The materials i used are from the classroom secessions at udacity and from [Suhas Srivat](https://github.com/suhassrivats) , and [Nicolas Hanout](https://github.com/nicolashanout/Show-Me-the-Data-Structures---UDACITY--/blob/master/explanation_3.md)
