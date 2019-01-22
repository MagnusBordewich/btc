import ecdsa
import json
import hashlib

# SECP256k1 is the Bitcoin elliptic curve
vk_string=open("vk.txt").read()
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string),ecdsa.SECP256k1)

# 
print('sk.__dict__',sk.__dict__)
print('sk.curve.__dict__',sk.curve.__dict__)
print('sk.curve.curve.__dict__',sk.curve.curve.__dict__)
print('sk.curve.generator.__dict__',sk.curve.generator.__dict__)
print('sk.privkey.__dict__',sk.privkey.__dict__)
# 
print('sk as ssl format string:',sk.to_pem())
