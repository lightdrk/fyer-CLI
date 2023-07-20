import hashlib

def hash_of(input_string):            
    input_bytes = input_string.encode('utf-8')
    sha_hash = hashlib.sha256(input_bytes).hexdigest()
    return sha_hash