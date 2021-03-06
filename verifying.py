import ecdsa
import json
import hashlib

# SECP256k1 is the Bitcoin elliptic curve
vk_string=open("vk.txt").read()
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string),ecdsa.SECP256k1)

message_hex = open("message.txt").read()
sig_hex = open("signature.txt").read()
message = bytes.fromhex(message_hex)
message_unserialised = json.loads(message)
sig = bytes.fromhex(sig_hex)
print("Checking signature")
print("Message:")
print(message_unserialised)
print("Signature:")
print(sig_hex)
print("Public key:")
print(vk_string)
try:
    vk.verify(sig, message)# True
    print('Verification passed')
except ecdsa.keys.BadSignatureError:
    print('Verification failed')


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
