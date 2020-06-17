
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



##### Acknowledgement

I want to acknowledge the help i got for this entire project, from the mentors at Udacity, the knowledge forum and chats on the student portal. The materials i used are from the classroom secessions at udacity and from [Suhas Srivat](https://github.com/suhassrivats) , and [Nicolas Hanout](https://github.com/nicolashanout/Show-Me-the-Data-Structures---UDACITY--/blob/master/explanation_3.md)
