import hashlib

def pbkdf2_encrypt(password, salt, iterations=100000, key_length=32):
    salt_bytes = salt.encode('utf-8')  
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_bytes, iterations, dklen=key_length)
    return key

if __name__ == "__main__":
    password = "my_ip"
    salt = ""

    key = pbkdf2_encrypt(password, salt)

    print("password:", password)
    print("salt:", salt)
    print("key:", key.hex())