from Crypto.Hash import SHA3_256
from Crypto.Random import get_random_bytes
from base64 import b64decode

hash_gen = SHA3_256.new()
with open("./sha256.py", "rb") as f_input:  # with WITH constructor
    # read the 1kB at the time...reading first 1024 bit
    hash_gen.update(f_input.read(1024))

print(hash_gen.digest())
print(hash_gen.hexdigest())
