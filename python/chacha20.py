# stream cipher to encrypt message
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

key = get_random_bytes(32)
cipher = ChaCha20.new(key=key)  # didn't pass the nonce

# b means allocating the byte not the string ..put the string as bytes
plaintext = b'this is the message to encrypt'
# we use the byte obj instead of str object

# for encryption we can skip the nonce and algorithm will make it by itself
# nonce = get_random_bytes(12) # 96 bit
ciphertext = cipher.encrypt(plaintext)

print(ciphertext)

print(cipher.nonce)

nonceb64 = b64encode(cipher.nonce)
# the output is kind of sequense bytes ..sequencde pof printable characters in byte
ciphertext64 = b64encode(ciphertext)
print(type(ciphertext64))
# so first we have to encode to hve specific bytes  and then decode to transform and have stream

# get bytes and check as streams of characters
print("the nonce is : " + nonceb64.decode())
print("the cipertext is : " + ciphertext64.decode())

# here we are at the recipient

########################################################
# the key has been exchanged in a secure way

# ciphertext64 and nonce64 have been recived frim the internet

cipher_dec = ChaCha20.new(key=key, nonce=b64decode(nonceb64))
ciphertext_extracted = b64decode(ciphertext64)
decrypted = cipher_dec.decrypt(ciphertext_extracted)


# it is sequence of bytes
print(f"this is a original message is :  {decrypted}")
