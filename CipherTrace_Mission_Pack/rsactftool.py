from Crypto.PublicKey import RSA

with open("public.pem", "rb") as f:
    key = RSA.import_key(f.read())

n = key.n
e = key.e

print(f"Modulus (n): {n}")
print(f"Exponent (e): {e}")

# LEVEL 2
from sympy import factorint

factors = factorint(n)
p, q = factors.keys()
print(f"Prime factors:\np = {p}\nq = {q}")

# LEVEL 3
from Crypto.Util.number import inverse

# Calculate Euler's totient function
phi_n = (p - 1) * (q - 1)

# Calculate private exponent
d = inverse(e, phi_n)
print(f"Private exponent (d): {d}")

# LEVEL 4
from Crypto.Util.number import long_to_bytes

# Convert ciphertext from hex to integer
ciphertext_hex = "a3f4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5c6d7e8f9"
c = int(ciphertext_hex, 16)

# Decrypt the ciphertext
m = pow(c, d, n)

# Convert the decrypted integer to bytes
plaintext_bytes = long_to_bytes(m)

# Convert bytes to string (assuming UTF-8 encoding)
plaintext = plaintext_bytes.decode('utf-8')
print(f"Decrypted message: {plaintext}")

# from Crypto.PublicKey import RSA
# # from Crypto.Util.number import inverse, long_to_bytes

# # === Step 1: Load RSA public key to get n and e ===
# with open("public.pem", "rb") as f:
#     key = RSA.import_key(f.read())

# n = key.n
# e = key.e

# print(f"Modulus (n): {n}")
# print(f"Public exponent (e): {e}")

# # === Step 2: Insert the prime factors of n (p and q) ===
# # Replace these with the actual prime factors you get from factoring n
# p = 3,5,7  # example: 1234567890123456789
# q = 11,19,511  # example: 9876543210987654321

# # === Step 3: Enter your ciphertext hex string here ===
# ciphertext_hex = "<your_ciphertext_hex_string_here>"

# # Convert ciphertext hex string to integer
# c = int(ciphertext_hex, 16)

# # === Step 4: Compute private exponent d ===
# phi = (p - 1) * (q - 1)
# d = inverse(e, phi)

# # === Step 5: Decrypt ciphertext ===
# m = pow(c, d, n)

# # Convert decrypted integer to bytes
# plaintext_bytes = long_to_bytes(m)

# # Decode bytes to string (ignores errors if any)
# plaintext = plaintext_bytes.decode('utf-8', errors='ignore')

# print("\nDecrypted message:")
# print(plaintext)
