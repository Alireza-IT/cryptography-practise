# instead way pycryptodome use hashlib
import hashlib

digest_object = hashlib.sha256()  # call directly instead of instaciaalis
digest_object .update(b"this is the first message")
