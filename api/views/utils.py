import hashlib


def hashOfHash(hash_list):

    hash_obj = hashlib.sha256()

    for hash_str in hash_list:
        hash_obj.update(bytes.fromhex(hash_str))

    result_hash = hash_obj.hexdigest()

    return result_hash

import hashlib


def hashFile(file_path):
    # Open the file in binary mode and read its contents
    with open(file_path, "rb") as f:
        file_contents = f.read()

    # Compute the hash of the file contents
    hash_value = hashlib.sha256(file_contents).digest()
    # print(hash_value)
    return hash_value