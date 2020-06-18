
##### Explanation_3 Huffman Coding

[//]: # (Image References)


[image1]: image1.png "Encoded text function"
[image2]: image2.png "Huffman_encoding"
[image3]: image3.png "Huffman decoding"


#### Requirement:

The `Huffman Coding` is a `lossless` data compression algorithm. A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information.A detailed explanantion of the Huffman can be found [here](https://medium.com/iecse-hashtag/huffman-coding-compression-basics-in-python-6653cdb4c476) and the [Udacity's](https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0/modules/a5f68248-862f-4a72-8682-24b86e2f6d61/lessons/a640374a-90af-40ad-85ff-1c6ce3948219/concepts/b97f3d67-ed9e-4759-8841-d13096f5cdd7) Problem 3: Huffman Coding, Overview on Data Compression which is detailed for this problem. 


#### Solution to problem: Code design

The concept behind Huffman Coding is that there has to be fewer bits assigned for frequently occurring letters and more bits for less frequent ones. Here is the approach i took for this problem. 

To encode the data first I counted the frequency of each charachter, then built heapafied tree where the leaf nodes were the charachters the depth of each charachter in the tree is determined by their frequency in the data.



##### Time Complexity

The time complexity for the Solution to the problem is `O(nlogn) `. The reason being; 

The time complexity for `Encoding` using the function `huffman_encoding(data)` is `O(nlogn) `.

1. Finding the frequency of each charachter is `O(n)` (loop once through the input).
    
2. Using a dictionary `node` which takes 2 `for loops` through the dictionary to find the 2 nodes with the lowest weight, in the dectionary to replace 2 nodes with 1 is `O(n)`. We need to repeat this process until we have 1 node left which is O(n-1) and thus overal end up with `=> O(n^2-n`).
3. When generating the code using `encoding = generate_huffman_code(tree)` on line 70 of `Problem 3 Huffman Coding.py` the time complexity is `O(nlogn)` where the the number of unique charachters in the data (the number of leafes in the tree)
4. When replacing the charachters in the string `encoded_data = encode(data, encoding)`, the time complexity is `O(n^2)` because here we are replacing charachters in the string.

The time complexity for `Decoding` using the function `huffman_decoding(data, tree)`is also `O(nlogn)`.

1. To generate the reverse code by calling `O(nlogn)` where in the the number of unique charachters in the data (the number of leafes in the tree). Also, the time complexity is `O(n^2) `where n is the length of the encoded data for building the string, loops over all charachters in the encoded data, and for each match with the reverse_code dictionary, it bulds a new string` O(n)`

Thus the total `time complexity` to the problem is `O(nlogn) `

#### Space Complexity

Space complexity is `O(n)` as we need a constant space to store each node. Therefore for `n` nodes, space complexity grows linearly, where `n` is the length of the string `=> decoding O(n)` .


##### Acknowledgement

I want to acknowledge the help i got for this entire project, from the mentors at Udacity, the knowledge forum and chats on the student portal. The materials i used are from the classroom secessions at udacity and from [Suhas Srivat](https://github.com/suhassrivats) , and [Nicolas Hanout](https://github.com/nicolashanout/Show-Me-the-Data-Structures---UDACITY--/blob/master/explanation_3.md)


