from Crypto.Hash import SHA256

# allocate hash object and dugest doesn't require any key and iv but can add the data at the first
# hash_gen = SHA256.new(data="even before the first part. ")

# # update funcion generator use to incrementally passed the additional data  to generator.....require data in form of byte
# hash_gen.update(b'this is the first part. ')
# hash_gen.update(b'this is the second part. ')
# hash_gen.update(b'this is the third part. ')


# # generate the digest
# print(hash_gen.hexdigest())
# print(hash_gen.digest())

# reading from the block and create hash
