
import hashlib
import datetime

# Get current time in GMT
gmt = datetime.datetime.now()


def calc_hash(data, timestamp):
    sha = hashlib.sha256()

    hash_str = data.encode('utf-8')+ str(timestamp).encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest()




class Block:
    
    def __init__(self, timestamp, data, previous_hash):
        
        self.timestamp = timestamp
        self.data = data
        self.previous = None
        self.previous_hash = previous_hash
        self.hash = calc_hash(str(data), self.timestamp)
        
    def __repr__(self):
        return (f"Block []: {repr(self.data)} \n" 
                f"Hash []: {repr(self.hash)} \n" 
                f"Previous Hash []: {repr(self.previous_hash)} \n" 
                f"{repr(self.timestamp)} \n" )

    
class BlockChain:
    def __init__(self):
        self.head = None
        
    def append(self, data, previous_hash):
        
        # add head to the tail of the block
        if self.head is None:
            self.head = Block(gmt, data, 0)
            return 
        
        new_head = Block(gmt, data, self.head.hash)
        new_head.previous = self.head
        self.head = new_head
        
    def size(self):
        
        # find the size of the linked list
        size = 0
        temporary = self.head
       
        while temporary:
            size += 1
            temporary = temporary.previous
        return size
    
    def to_list(self):
        # get the node/blocks in the linkedlist
        output = []
        block = self.head
        
        while block:
            output.append(block)
            block = block.previous
            
        return output


# Test cases data
data_1 = "We are going to encode this string of data!"
data_2 = "Udacity Data Stracture Nanodegree is tough...but totaly woth it"
data_3 = "Happy with the results so far!! "
data_4 = "I made the right call with this program"
data_5 = "Thank you Udacity."


data_6 = "Mercedes"
data_7 = "Tesla"
data_8 = "Ford"


print("Test case 1")
print("Test with empty Block chain")
test_1 = BlockChain()
print('Current size of Blockchain is {}'.format(test_1.size()))
print('What is at the top of the Blockchain: {}'.format(test_1.head))
print()

print("Test case 2")
print("Test with 5 items added to Blockchain \n")

test_1 = BlockChain()
test_1.append(data_1, 0)
test_1.append(data_2, calc_hash(data_1, gmt))
test_1.append(data_3, calc_hash(data_2, gmt))
test_1.append(data_4, calc_hash(data_3, gmt))
test_1.append(data_5, calc_hash(data_4, gmt))

print('Current size of Blockchain is {}'.format(test_1.size()))
print('What is at the top of the Blockchain: {}'.format(test_1.head))

print()
for item in test_1.to_list():
    print("Items in the blockchain are;\n")
    print(item)

    
print("Test case 3")
print("Test with 3 items added to Blockchain \n")

cars = BlockChain()
cars.append(data_6, 0)
cars.append(data_7, calc_hash(data_6, gmt))
cars.append(data_8, calc_hash(data_7, gmt))


print('Current size of Blockchain is {}'.format(cars.size()))
print('What is at the top of the Blockchain: {}'.format(cars.head))

print()
for item in cars.to_list():
    print("Items in the blockchain are;\n")
    print(item)



"""OUTPUT

Test case 1
Test with empty Block chain
Current size of Blockchain is 0
What is at the top of the Blockchain: None

Test case 2
Test with 5 items added to Blockchain 

Current size of Blockchain is 5
What is at the top of the Blockchain: Block []: 'Thank you Udacity.' 
Hash []: '37d897a3290fdf52ce0cefcd2aee6ff7f546cc316c18828d7f2b3593b8f5da5d' 
Previous Hash []: '472766b6a6b7da7b20c16da6c48ce75074c86d04990a38e5d00b39cc8ba95eac' 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 


Items in the blockchain are;

Block []: 'Thank you Udacity.' 
Hash []: '37d897a3290fdf52ce0cefcd2aee6ff7f546cc316c18828d7f2b3593b8f5da5d' 
Previous Hash []: '472766b6a6b7da7b20c16da6c48ce75074c86d04990a38e5d00b39cc8ba95eac' 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 

Items in the blockchain are;

Block []: 'I made the right call with this program' 
Hash []: '472766b6a6b7da7b20c16da6c48ce75074c86d04990a38e5d00b39cc8ba95eac' 
Previous Hash []: '984d808adf3422e519880af3cf688ab0db1e82862f921fe58b65337820e0e44a' 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 

Items in the blockchain are;

Block []: 'Happy with the results so far!! ' 
Hash []: '984d808adf3422e519880af3cf688ab0db1e82862f921fe58b65337820e0e44a' 
Previous Hash []: '35d933864aecfdcc5b6444eb593abbec9aea06c37963f9f194464e7061141c55' 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 

Items in the blockchain are;

Block []: 'Udacity Data Stracture Nanodegree is tough...but totaly woth it' 
Hash []: '35d933864aecfdcc5b6444eb593abbec9aea06c37963f9f194464e7061141c55' 
Previous Hash []: '3337416dc5a70520d89911bb21e5f3f2429928679742738ea55bb913dfbe836a' 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 

Items in the blockchain are;

Block []: 'We are going to encode this string of data!' 
Hash []: '3337416dc5a70520d89911bb21e5f3f2429928679742738ea55bb913dfbe836a' 
Previous Hash []: 0 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 

Test case 3
Test with 3 items added to Blockchain 

Current size of Blockchain is 3
What is at the top of the Blockchain: Block []: 'Ford' 
Hash []: 'e53b0087b4b3e039a78ac4cc5cdc9a032499cc1ac70c888b6101c3db1bb17d62' 
Previous Hash []: '07505ea76d161237f5f82eecec5348cc9faaf225c522d1c3346f7846b225c9ab' 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 


Items in the blockchain are;

Block []: 'Ford' 
Hash []: 'e53b0087b4b3e039a78ac4cc5cdc9a032499cc1ac70c888b6101c3db1bb17d62' 
Previous Hash []: '07505ea76d161237f5f82eecec5348cc9faaf225c522d1c3346f7846b225c9ab' 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 

Items in the blockchain are;

Block []: 'Tesla' 
Hash []: '07505ea76d161237f5f82eecec5348cc9faaf225c522d1c3346f7846b225c9ab' 
Previous Hash []: '06b2fe3925ab53b8becf4923ac38221e1f114a1ddf69b4b0152bf437a9a7a0d4' 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 

Items in the blockchain are;

Block []: 'Mercedes' 
Hash []: '06b2fe3925ab53b8becf4923ac38221e1f114a1ddf69b4b0152bf437a9a7a0d4' 
Previous Hash []: 0 
datetime.datetime(2020, 6, 16, 20, 25, 52, 212288) 

"""




