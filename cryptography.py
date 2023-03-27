from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Really confidential data")
print(token)

# really weird, why it's only working in python console?
