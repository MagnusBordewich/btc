import hashlib
import json
import time

class Blockchain(object):
    def __init__(self):
        self.chain=[]
        block_0 = {
            'index': 0,
            'time': time.time(),
            'block_data': 'This is the first block. The Time 14/Jan/19 Rebels hatch bill to delay Brexit.',
            'hash_of_previous_block': None
        }
        self.add_new_block(block_0)
        
    def add_new_block(self,block):
        print('New block created. Index: ',block['index'])
        print('New block data: ',block['block_data'])
        if self.verify(block,block['index']-1):
            self.chain.append(block)
            #print('Hash of previous block:',block['hash_of_previous_block'])
            print('New block added')
            print('')
            return block
        else:
            print("New block not added: failed verification")
            return block
        
    def hash(self,block):
        block_serialised = json.dumps(block, sort_keys=True).encode('utf-8')
        return hashlib.sha256(block_serialised).hexdigest()
    
    def last_block(self):
        return self.chain[-1]
    
    def verify(self,block,index_of_previous_block):
        if index_of_previous_block==-1:
            print(' Verification passed: initial block')
            return True
        elif block['hash_of_previous_block']==self.hash(self.chain[index_of_previous_block]):
            print(' Verification passed:')
            print(' block_prev_hash ',block['hash_of_previous_block'])
            print(' actual_prev_hash',self.hash(self.chain[index_of_previous_block]))
            return True
        else:
            print(' Verification failed:')
            print(' block_prev_hash ',block['hash_of_previous_block'])
            print(' actual_prev_hash',self.hash(self.chain[index_of_previous_block]))
            return False
        
        
    def verify_chain(self):
        for i in reversed(range(len(self.chain))):
            print('')
            print('Checking block',i)
            step_verification = self.verify(self.chain[i],i-1)
            if step_verification==False:
                return False, i
        return True, None

MagCoin = Blockchain()

block_1 = {
    'index': 1,
    'time': time.time(),
    'hash_of_previous_block': MagCoin.hash(MagCoin.last_block()),
    'block_data': ["This is the second block.",42]
    }
MagCoin.add_new_block(block_1)

for i in range(3):
    previous_block=MagCoin.last_block() 
    my_block = {
    'index': previous_block['index']+1,
    'time': time.time(),
    'hash_of_previous_block': MagCoin.hash(previous_block),
    'block_data': ["This is another block.",i]
    }
    MagCoin.add_new_block(my_block)
    
print('Chain verification: ',MagCoin.verify_chain())
# bad_block = MagCoin.chain[2]
# print(bad_block)
# bad_block['block_data']=  ["This is another block!",0]
# print(bad_block)
# MagCoin.chain[2] = bad_block
# print('Chain verification: ',MagCoin.verify_chain())
