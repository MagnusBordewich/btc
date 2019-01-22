import sys
import uuid
from Crypto.Hash import SHA256

com, key, message = sys.argv[1], sys.argv[2], sys.argv[3]
#nonce = uuid.uuid4().bytes
check = SHA256.new(bytes.fromhex(key))
check.update(message.encode('utf8'))
print('com:',com)
print('key:',key)
print('message:',message)
print('check:',check.hexdigest())
if check.hexdigest()==com:
    print('Verification successful')
else:
    print('Verification failed')