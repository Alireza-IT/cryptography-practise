from Crypto.Cipher import ChaCha20

# attacker must know the structure of the plaintext
####
from Crypto.Random import get_random_bytes

plaintext = b"This is a string where there are numbers 123456. Bye!"

# sender
# encrypt with ChaCha20
key = get_random_bytes(32)
cipher = ChaCha20.new(key=key)  # nonce is generating automatically
ciphertext = cipher.encrypt(plaintext)  # bytes: which is unmodifiable

# sent the ciphertext

#################

# attacker side (with some helps) : MitM
index = plaintext.index(
    b"1"
)  # locate where to he want to change .what is index of byte to change so use index function.
print(index)
print(plaintext[index])  # give hexidecimal valule

new_value = b"2"  # working with byte so use b in front of this
print(new_value)
print(ord(new_value))  # ord return ASCII code
#'1' 49
#'2' 50 --> last two bits will change

# build the mask
# a XOR b = c --> a XOR c = b
# old value and new value
# build an editable byte array and update it with the mask
# do not use XOR with bytes
mask = plaintext[index] ^ ord(new_value)
print(mask)  # 0011
cipher_array = bytearray(ciphertext)  # becuase the byte is unmodifiable
cipher_array[index] = cipher_array[index] ^ mask

print(cipher_array[index])
print(ciphertext[index])

print("          " + str(ciphertext))
print(cipher_array)

# MitM sends this new ciphertext to the recipient

####
# check by decrpytion
cipher_dec = ChaCha20.new(key=key, nonce=cipher.nonce)  # first create dec object
print(cipher_dec.decrypt(cipher_array))
