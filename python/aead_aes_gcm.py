
# two operation at the same time ecnryption with aes and computation of a MAC
# only for authentication plus integrity and encryption
# aead : encrypt the confidential part
# aead: compute the mac on auth-only + confidentiality part

# create a gcm mdoe aes 256 cipher
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json

key = get_random_bytes(16)
# gcm is using the nonce which is randomly generated
cipher = AES.new(key, AES.MODE_GCM)


# data
auth_only_data = b"this is the part to authenticate / header"
confidential_data = b'this part should be kept secret'


# pass the header ==> update function
cipher.update(auth_only_data)  # only part need auth
# return two outputs ciphertext and tag which compute on concatincatino of auth and confidential data
ciphertext, tag = cipher.encrypt_and_digest(confidential_data)
# output is in bytes


# pack data
# new way of dictionary
keys = ["ciphertext", "tag", "header", "nonce"]  # we skip the algorithm name
# binary string which is not mapped to aschii characters and produce the byte and the decode to get string
# data = [base64.b64encode(ciphertext).decode(),
#         base64.b64encode(tag).decode(), auth_only_data.decode(), base64.b64encode(cipher.nonce()).decode()]  # header is already in byte just to decode
data = [base64.b64encode(x).decode() for x in (
    ciphertext, tag, auth_only_data, cipher.nonce)]
# to combine keys and data we used zip
packed_data = json.dumps(dict(zip(keys, data)))

print(packed_data)

# decode trasfer byte to string provided by all bytes are printable
# printable string which is str class can convert into byte by encode

# assume we recived the packet data securelt

unpacked_data = json.loads(packed_data)

# print(type(unpacked_data["nonce"])) ==> is string


# create cipher pass nonce

cipher_verification = AES.new(
    key, AES.MODE_GCM, nonce=base64.b64decode(unpacked_data["nonce"]))

# pass the header
# base64 need byte so we use the encode
cipher_verification.update(base64.b64decode(unpacked_data["header"]))

# check tag and obtain plaintext
try:
    plaintext = cipher_verification.decrypt_and_verify(base64.b64decode(
        unpacked_data["ciphertext"], base64.b64decode(unpacked_data["tag"])))  # verify by the header that we already added
except ValueError:
    print("ERROR: the mac is incorrect ")

print(f"the mac is correct and the plaintext is : {plaintext}")
