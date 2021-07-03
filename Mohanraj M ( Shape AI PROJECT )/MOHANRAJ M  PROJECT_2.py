import hashlib
import time

message = str(input("Enter some text for change into the hash:"))

md_5 = hashlib.md5(message.encode()).hexdigest()

sha_512 = hashlib.sha512(message.encode()).hexdigest()

sha_256 = hashlib.sha256(message.encode()).hexdigest()

time.sleep(3)

print("\n ***************************************************************************************************")

time.sleep(2)

print("\n The MD5 hash of given string : " + md_5)

time.sleep(2)

print("\n The SHA256 hash of given string : " + sha_256)

time.sleep(2)

print("\n The SHA512 hash of given string : " + sha_512)

time.sleep(2)

print("\n ***************************************************************************************************")

