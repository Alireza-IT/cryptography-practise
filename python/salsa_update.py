from Crypto.Cipher import Salsa20
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes


# these are bytes
plaintext = b'this is the new message.'
plaintext2 = b' this is another message'

# encrypt with update

key = get_random_bytes(16)

cipher = Salsa20.new(key=key)  # nonce is automatically generated

ciphertext = cipher.encrypt(plaintext)
ciphertext += cipher.encrypt(plaintext2)

nonce = cipher.nonce  # this is a requirement

print(nonce)

##########
# we are at the recipient here
cipher_dec = Salsa20.new(key=key, nonce=nonce)

plaintext_decrypted = cipher_dec.decrypt(ciphertext)  # work incrementally


print(f'this is decryptiion : {plaintext_decrypted}')

# this incremental encryption only with stream cipher because we don't have padding here
