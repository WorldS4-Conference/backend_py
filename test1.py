import hashlib

input_str = "673a87e781ca301277c72a534a60a5009ce1401936c9ce6c40be915ceb9fc1b3" + "soham2019@iiitkottayam.ac.in"
hash_obj = hashlib.sha256(input_str.encode())
result_hash = hash_obj.hexdigest()

print("Result hash:", result_hash)
