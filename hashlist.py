# A series of blocks of data created in sequential order with hash of the previous block contained.

import hashlib
import json
    
block_0 = {
    'block_data': 'This is the first bl0ck. The Time 14/Jan/19 Rebels hatch bill to delay Brexit.',
    'hash_of_previous_block': None
}

block_0_serialised = json.dumps(block_0, sort_keys=True).encode('utf-8')
block_0_hash = hashlib.sha256(block_0_serialised).hexdigest()

print(block_0_serialised)
print(block_0_hash)

block_1 = {
    'hash_of_previous_block': block_0_hash,
    'block_data': ["This is the second block.",42]
}

block_1_serialised = json.dumps(block_1, sort_keys=True).encode('utf-8')
block_1_hash = hashlib.sha256(block_1_serialised).hexdigest()

print(block_1_serialised)
print(block_1_hash)

block_2 = {
    'hash_of_previous_block': block_1_hash,
    'block_data': ["This is the third block.",{'Number':42, 'Size':'XXL'}]
}

block_2_serialised = json.dumps(block_2, sort_keys=True).encode('utf-8')
block_2_hash = hashlib.sha256(block_2_serialised).hexdigest()

print(block_2_serialised)
print(block_2_hash)


