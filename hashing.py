import hashlib
import json

message = 'Hello W0rld'
message_hash = hashlib.sha256(message.encode()).hexdigest()
print(message_hash)

data_block = {
    'block_text': 'This is the first block. The Times 14/Jan/19 Rebels hatch bill to delay Brexit.',
    'block_data': [123,234,321,345,645,235,765,234,7456,746,5245,456,568,456,345,457,23],
    'block_meta_data_1': 123,
    'block_meta_data_2': '15/01/2019'
}

data_block_serialised = json.dumps(data_block, sort_keys=True).encode('utf-8')
data_block_hash = hashlib.sha256(data_block_serialised).hexdigest()

print(data_block_serialised)
print(data_block_hash)

data_block_2 = {
    'block_meta_data_1': 123,
    'block_text': 'This is the first block. The Times 14/Jan/19 Rebels hatch bill to delay Brexit.',
    'block_data': [123,234,321,345,645,235,765,234,7456,746,5245,456,568,456,345,457,23],
    'block_meta_data_2': '15/01/2019'
}
data_block_2_serialised = json.dumps(data_block_2, sort_keys=True).encode('utf-8')
data_block_2_hash = hashlib.sha256(data_block_2_serialised).hexdigest()

print(data_block_2_hash)