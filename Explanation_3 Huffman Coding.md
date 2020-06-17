
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



##### Acknowledgement

I want to acknowledge the help i got for this entire project, from the mentors at Udacity, the knowledge forum and chats on the student portal. The materials i used are from the classroom secessions at udacity and from [Suhas Srivat](https://github.com/suhassrivats) , and [Nicolas Hanout](https://github.com/nicolashanout/Show-Me-the-Data-Structures---UDACITY--/blob/master/explanation_3.md)
