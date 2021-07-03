import hashlib
import time

#Using of hashlib module we can perform more crptography things

print("Convert the string into MD5 Hash \n \n")

#Getting string as input from user

userInput = str(input("Enter your string for change into hashes:"))

#Using encode() function in hashlib for encode the given content , At first that md5 indicates that type of making hashes


finalOutput = hashlib.md5(userInput.encode())

print("\nwaiting for few sec , The encoding is on process")

time.sleep(3)

print("\n ******************************************************************")

print("\n The hash values of your string: " + finalOutput.hexdigest())

print("\n ******************************************************************")
