import sys
import uuid
from Crypto.Hash import SHA256
import hashlib

message = sys.argv[1]
nonce = uuid.uuid4().bytes
com = SHA256.new(nonce)
com.update(sys.argv[1].encode('utf8'))
print('com:',com.hexdigest())
print('key:',nonce.hex())

com2 = hashlib.sha256(nonce+message.encode()).hexdigest()
print(com2)