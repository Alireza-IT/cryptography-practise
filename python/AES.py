from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
# encrypt a file
key = get_random_bytes(32)  # 256 bit

cipher = AES.new(key, AES.MODE_CBC)  # IV is generated in random automatically
Iv = cipher.IV

plaintext = b"this is the AES plaintext"
print(AES.block_size)  # 16 bytes 128 bits

padding_plain = pad(plaintext, AES.block_size)  # PKCS5
print(padding_plain)  # x07\x07\x07\x07\x07\x07\x07 is 7 bytes of padding

# ciphertext = cipher.encrypt(padding_plain)
# print(ciphertext)

f_input = open("chacha20.py", "rb")
# use read function for reading the entire file
ciphertext = cipher.encrypt(pad(f_input.read(), AES.block_size))
print(ciphertext)


##############
# we are at the recipient
cipher_dec = AES.new(key, AES.MODE_CBC, Iv)
decrypted = cipher_dec.decrypt(ciphertext)

# print(f"this is decryption : {decrypted}")
unpad_decrypted = unpad(decrypted, AES.block_size)

print(f"this is decryption : {unpad_decrypted}")

# without the iv the first block is wrong but rest is correct
# openssl is slower than pycryptodome
# openssl is more best for implementation for years and years.
