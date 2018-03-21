import hashlib
import datetime
class Block:
    def __init__(self, index, timestamp, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        ## TODO: generate this value with the hash function
        self.currentHash = hashlib.sha256()
        # add a timestamp value using a library or something
        self.timestamp = ''
        self.nonce = 0

    ## TODO: Add hashing methods to generate the hash value for the block
    def hashBlock(self):
        self.nonce = self.nonce + 1
        self.currentHash.update(b'a')


b = Block(12345,'231sadaddsaf')
print(b.currentHash)
print(b.hashBlock())
print(b.currentHash)