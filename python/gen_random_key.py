
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

# gererate the random key
# 16 byte means 128 bit of key
random = get_random_bytes(16)
print(random)

print(type(random))  # it is bytes class
# using b64encode to get stream
print(b64encode(random))
