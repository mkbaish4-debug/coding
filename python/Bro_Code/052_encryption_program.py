import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

# ENCRYPT
print("*" * 30)
print("Encryption program")

print("*" * 30)
message = input("Enter the message you want to encrypt: ")
encrypted_mssg = ""
for character in message:
    index = chars.index(character)
    encrypted_mssg += keys[index]

print(f"Original message: {message}")
print(f"Ecrypted message: {encrypted_mssg}")


print("*" * 30)
message = input("Enter the message you want to decrypt: ")
decrypted_mssg = ""
for character in message:
    index = keys.index(character)
    decrypted_mssg += chars[index]

print(f"Encrypted message: {message}")
print(f"Decrypted message: {decrypted_mssg}")
