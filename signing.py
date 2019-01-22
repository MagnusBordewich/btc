import ecdsa
import json
import hashlib

# SECP256k1 is the Bitcoin elliptic curve
sk_string=open("sk.txt").read()
sk = ecdsa.SigningKey.from_string(bytes.fromhex(sk_string),ecdsa.SECP256k1)

block_0 = {
    'block_data': 'This is the first block. The Time 14/Jan/19 Rebels hatch bill to delay Brexit.',
    'hash_of_previous_block': None
}
block_serialised = json.dumps(block_0, sort_keys=True).encode('utf-8')

sig = sk.sign(block_serialised)

open("message.txt","w").write(block_serialised.hex())
open("signature.txt","w").write(sig.hex())

print(block_0)
print("Signature: "+sig.hex())
# print(sig)
# print(vk.verify(sig, b"message"))
# 
# print('sk.__dict__',sk.__dict__)
# print('sk.curve.__dict__',sk.curve.__dict__)
# print('sk.curve.curve.__dict__',sk.curve.curve.__dict__)
# print('sk.curve.generator.__dict__',sk.curve.generator.__dict__)
# print('sk.privkey.__dict__',sk.privkey.__dict__)
# 
# print('sk as ssl format string:',sk.to_pem())
