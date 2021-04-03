from Crypto.Random import get_random_bytes
# use hash function in hmaxc function..hmac is algorithm that use sha512 internally
from Crypto.Hash import HMAC, SHA512
import json
import base64
# gen message

msg = b"this is the message.this is the message.this is the message.this is the message.this is the message.this is the message."  # sequece of bytes


# instance hmac object to compute the digest of message ....
key = get_random_bytes(16)
hmac_gen = HMAC.new(digestmod=SHA512, key=key)
hmac_gen.update(msg)  # use hmac in incremental mode


print(hmac_gen.hexdigest())


# pack data into json object
# send all data together ....pass the MAC and original message at the same time
# generate the sequece of bytes and output as string
mac = base64.b64encode(hmac_gen.digest()).decode()
# inorder to pack all data and as we have to pass dictionary to it
packed_data = json.dumps({"message": msg.decode(), "MAC": mac})

print(packed_data)


# byte_object.decode()====> reaturn a string and none printable character

# here we are at the reciver

# packed datas are received by some tools
#
# unpack data
unpacked_data = json.loads(packed_data)  # we have dictinary
print(type(unpacked_data["message"]))  # is string
print(unpacked_data["MAC"])


hmac_verifier = HMAC.new(key=key, digestmod=SHA512)

# need byte that why we use encode
hmac_verifier.update(unpacked_data["message"].encode())
print(hmac_verifier.hexdigest())
# not polite way use below

# verify MAC
print(type(base64.b64decode(unpacked_data["MAC"])))
try:
    hmac_verifier.verify(base64.b64decode(unpacked_data["MAC"]))
except ValueError:
    print("error MAC verification is failed")
print("mac verification not failed")

# base64 decode and encode produce the bytes

# hexdigest get 1 byte into 2 characters
# base64 is 6 bits into 8 bits
# base64 is the form to generate printable characters from generic bytes but not excellent performance

# to make  byte object to modifiable
modified_MAC = bytearray(base64.b64decode(unpacked_data["MAC"]))
print(modified_MAC[0])

# bytes are unmodifiable
modified_MAC[0] = 11
print(modified_MAC[0])

try:
    hmac_verifier.verify(base64.b64decode(modified_MAC))
except ValueError:
    print("error MAC verification is failed")

print("mac verification not failed")
