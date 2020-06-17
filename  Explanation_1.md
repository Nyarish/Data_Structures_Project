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

##### Acknowledgement

I want to acknowledge the help i got for this entire project, from the mentors at Udacity, the knowledge forum and chats on the student portal. The materials i used are from the classroom secessions at udacity and from [Suhas Srivat](https://github.com/suhassrivats)