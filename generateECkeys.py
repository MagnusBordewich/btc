import ecdsa

# SECP256k1 is the Bitcoin elliptic curve
sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) 
vk = sk.get_verifying_key()

sig = sk.sign(b"message")

if vk.verify(sig, b"message"):
    sk_string=sk.to_string().hex()
    vk_string=vk.to_string().hex()
    
    print("\nMy private/signing key: "+sk_string+"\n")
    print("My public/verification key: "+vk_string+"\n")


    open("sk.txt","w").write(sk_string)
    open("vk.txt","w").write(vk_string)
# to retreive keys for later use:
# sk = SigningKey.from_string(open("sk.string").read())
# vk = VerifyingKey.from_string(open("vk.string").read())
