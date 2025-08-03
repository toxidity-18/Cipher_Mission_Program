

````markdown
# 🕵️‍♂️ Multi-Level Crypto Puzzle Solver

This Python script is a step-by-step cryptography challenge solver that decodes hidden messages using various encoding, encryption, and steganographic techniques. It progresses through **4 security challenge levels**, each building on common real-world techniques used in CTFs (Capture The Flag) or cryptographic puzzles.

---

## 📜 Level 1: Base64 Decoding

```python
import base64
print(base64.b64decode("VGhlIGRyb3AgbG9jYXRpb24gaXMgaGlkZGVuIGluIHRoZSBuZXh0IGZpbGUu"))
````

* Decodes a Base64-encoded string.
* The message reveals a clue pointing to another file (`message.txt`) that contains the next piece of the puzzle.

---

## 🔐 Level 2: ROT13 Cipher

```python
def rot13(text): ...
with open("message.txt") as f:
    print(rot13(f.read()))
```

* Implements and applies a **ROT13** substitution cipher to decrypt `message.txt`.
* This reveals a hint or perhaps another encrypted message.

---

## 🔓 Level 3: AES Decryption with Brute Force

```python
from Crypto.Cipher import AES
...
for b in range(256):
    key = known_key_prefix + bytes([b]) + b'\x00' * 7
    ...
```

* Reads `aes_encrypted.bin`, splits IV and ciphertext.
* Brute-forces the **last byte of a partially known 16-byte AES key**.
* Attempts to decrypt using AES-CBC mode and `unpad()`s the result.
* Prints out the successfully decrypted plaintext when the correct key is found.

---

## 🖼️ Level 4: Steganography in PNG

```python
with open("image.png", "rb") as f:
    data = f.read()
...
print(base64.b64decode(hidden_b64).decode())
```

* Reads a PNG file (`image.png`).
* Extracts all data **after the PNG magic number** `\x89PNG\r\n\x1a\n`.
* Decodes the hidden Base64-encoded string embedded after the PNG header.
* Prints the final decoded hidden message.

---

## 🧩 Summary

This program walks through various classic CTF-style decoding stages:

| Level | Technique       | File Used           | Concept Applied                   |
| ----- | --------------- | ------------------- | --------------------------------- |
| 1     | Base64 Decoding | —                   | Simple data encoding              |
| 2     | ROT13 Cipher    | `message.txt`       | Substitution cipher               |
| 3     | AES Brute Force | `aes_encrypted.bin` | Cryptanalysis on AES keys         |
| 4     | PNG Stego       | `image.png`         | Steganography + Base64 extraction |

---

## 🧠 Requirements

* Python 3.x
* `pycryptodome` (for AES decryption)

Install dependencies:

```bash
pip install pycryptodome
```

---

## 💡 Usage

Place the required files (`message.txt`, `aes_encrypted.bin`, `image.png`) in the same directory as the script and run:

```bash
python Cracked_Version.py
```

---

## 🔒 Educational Purpose Only

> This project is intended for **educational and ethical hacking learning purposes** only. Do not use these techniques for unauthorized access or illegal activities.

---
