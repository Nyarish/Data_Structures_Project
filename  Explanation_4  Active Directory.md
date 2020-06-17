
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



##### Acknowledgement

I want to acknowledge the help i got for this entire project, from the mentors at Udacity, the knowledge forum and chats on the student portal. The materials i used are from the classroom secessions at udacity and from [Suhas Srivat](https://github.com/suhassrivats) , and [Nicolas Hanout](https://github.com/nicolashanout/Show-Me-the-Data-Structures---UDACITY--/blob/master/explanation_3.md)
