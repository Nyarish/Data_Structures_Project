
import sys
import heapq

# Based on the Huffman dicitionary, generate unique binary code for each character of our string message
def encoded_text(huffman_dict, data):
    huff_code = ''
    
    for _ in data:
        huff_code += str(huffman_dict[_])
    return huff_code


def huffman_encoding(data):
    
    # Create dictionary to store charcters/symbols and frequency
    huff = {}
    
    global huffman_dict
    huffman_dict = {}
    
    # Determine the frequency of each character in the message
    for char in data:
        huff[char] = huff.get(char, 0) + 1
    
    # Build a huffman tree heap
    heap = [[frequency,[character, '']] for character, frequency in huff.items()]  
    heapq.heapify(heap)
    
    if len(heap) == 1:
        huffman_dict[heap[0][1][1]] = str(heap[0][0])
        huffcode = encoded_text(huffman_dict, data)
        return huffcode, heap
    
    # Build and sort a list of nodes in the order lowest to highest frequencies. 
    # where a node that has lower frequency should have a higher priority to be popped-out.
    
    while len(heap) > 1:
        left_child = heapq.heappop(heap)
        right_child = heapq.heappop(heap)
    
        # For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child
        for value in left_child[1:]:
            value[1] = '0'+ value[1]
        for value in right_child[1:]:
            value[1] = '1' + value[1]
        
        heapq.heappush(heap, [left_child[0] + right_child[0]] + left_child[1:] +right_child[1:])
    
    # Make a dictionary of a char and its binary code
    huffman_list = left_child[1:] + right_child[1:]
    huffman_dict = {_[0]: str(_[1]) for _ in huffman_list}
    
    huffcode = encoded_text(huffman_dict, data)
    return huffcode, heap

def huffman_decoding(data,tree):
    decoded_text = ''
    current_code = ''
    
    for bit in data:
        current_code += bit
        if current_code in huffman_dict.values():
            for key in huffman_dict:
                if current_code == huffman_dict[key]:
                    decoded_text += key
                    current_code = ""
                            
    return decoded_text

if __name__ == "__main__":
    codes = {}
    
    # Test case 1
    print("Test case 1")

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    print("_________________________________________")
    # Test case 2
    print("Test case 2")

    a_great_sentence = "Udacity is best MOOCK out there..."

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    print("_________________________________________")
    # Test case 3
    print("Test case 3")

    a_great_sentence = "Data Structure And Algorithm is a touch cooky but totaly worth it"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


"""OUTPUT

Test case 1
The size of the data is: 69

The content of the data is: The bird is the word

The size of the encoded data is: 36

The content of the encoded data is: 1110000100011011101010100111111001001111101010001000110101101101001111

The size of the decoded data is: 69

The content of the encoded data is: The bird is the word

_________________________________________
Test case 2
The size of the data is: 83

The content of the data is: Udacity is best MOOCK out there...

The size of the encoded data is: 44

The content of the encoded data is: 0010101011010000101001111010000110011110011100100111111001101110001000011001100010000111100110110001101110101011001111100001111111011101110

The size of the decoded data is: 83

The content of the encoded data is: Udacity is best MOOCK out there...

_________________________________________
Test case 3
The size of the data is: 114

The content of the data is: Data Structure And Algorithm is a touch cooky but totaly worth it

The size of the encoded data is: 60

The content of the encoded data is: 01010001101100110111010101110100110101011111010101001011100111010011000100101111110100110000011101001100100011100000011111111000110001111101101111100011010101110000111101110010010111101011011101011010101101111100011100110100001011011101000001100111000001110001110

The size of the decoded data is: 114

The content of the encoded data is: Data Structure And Algorithm is a touch cooky but totaly worth it

"""





