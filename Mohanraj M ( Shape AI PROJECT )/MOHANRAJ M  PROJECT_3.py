import hashlib

#Here the pdkdf is password-based key derivation function 2 with that hmac "pseudorandom" function

dk=hashlib.pbkdf2_hmac('sha256',b'Shape ai',b'salt',5)

print("\n *************************************************")

print("\n  The final output hash of given is: " + dk.hex())

print("\n *************************************************")
