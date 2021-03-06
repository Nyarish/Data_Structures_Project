
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


##### Acknowledgement

I want to acknowledge the help i got for this entire project, from the mentors at Udacity, the knowledge forum and chats on the student portal. The materials i used are from the classroom secessions at udacity and from [Suhas Srivat](https://github.com/suhassrivats) , and [Nicolas Hanout](https://github.com/nicolashanout/Show-Me-the-Data-Structures---UDACITY--/blob/master/explanation_3.md)
