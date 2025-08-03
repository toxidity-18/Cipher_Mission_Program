# ELEVEL 1
import base64
print(base64.b64decode("VGhlIGRyb3AgbG9jYXRpb24gaXMgaGlkZGVuIGluIHRoZSBuZXh0IGZpbGUu"))
# LEVEL 2
def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 13
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

with open("message.txt") as f:
    print(rot13(f.read()))

with open("aes_encrypted.bin", "rb") as f:
    data = f.read()
iv = data[:16]
ciphertext = data[16:]
known_key_prefix = bytes.fromhex("9a5c1b7f82a47613")
# Brute force for encryption keys LEVEL 3
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import itertools

# Try basic brute force on the last 1 byte (expand if needed)
for b in range(256):
    key = known_key_prefix + bytes([b]) + b'\x00' * 7  # dummy padding
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        print(decrypted.decode())
        break
    except:
        continue
# LEVEL 4
with open("image.png", "rb") as f:
    data = f.read()

# Extract after PNG magic bytes
b64_start = data.find(b'\x89PNG\r\n\x1a\n') + 8
hidden_b64 = data[b64_start:]
import base64
print(base64.b64decode(hidden_b64).decode())
