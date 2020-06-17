
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
