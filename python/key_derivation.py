# KDF take the password and generate the good key and uses the salt for freshness and imporvment statistical
# delay attacker and have iteration parameters + increase the memory used
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
password = b"passw0rd"
salt = get_random_bytes(16)  # at least 16 bytes
# iteration logins and 32 is length of key
key = scrypt(password, salt, 32, N=2**20, r=8, p=1)


print(key)
#
