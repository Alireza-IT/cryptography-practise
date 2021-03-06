import os

os.environ[
    "PWNLIB_NOTERM"
] = "True"  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ["PWNLIB_SILENT"] = "True"

from pwn import *

from mysecrets import HOST, PORT


# first connect to the server and get a response
server = remote(HOST, PORT)  # object manages the connections

input = b"This is a message"

server.send(input)
ciphertext = server.recv(1024)  # recived 1024 bytes
print(ciphertext.hex())

server.close()

# print some info

# message = "This is what I received: " + input + " -- END OF MESSAGE" generated by server
s1 = "This is what I received: "
# Aes block size = 16 so the first 16 bytes (This is what I r) and second block is (eceived: ) which are our input
# if you want to compare two entire blocks to we are adding some data to to align the blocks
s2 = " -- END OF MESSAGE"
print(len(s1))

input = (
    "A" * 512
)  # because block aes is 16 bytes long we have to along to that.by random data

# for checking again
server = remote(HOST, PORT)

server.send(input)
ciphertext = server.recv(1024)
c_hex = ciphertext.hex()

print(c_hex[64:96])
print(c_hex[96:128])

if ciphertext[32:48] == ciphertext[48:64]:
    print("The server used ECB")
else:
    print("The server used CBC")

# second part in byte start from 32 to 48


server.close()


# "This is what I received: "
# AES block size = 16
#
# This is what I r
# eceived: AAAAAAA
# aaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaa


"a" * 16
"a" * 16
