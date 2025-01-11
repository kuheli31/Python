def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift  # Reverse shift for decryption
    
    result = ""
    for char in text:
        if char.isalpha():  # Only process letters
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char  # Keep non-letters unchanged
    return result

# Example usage
encrypted = caesar_cipher("Hello, World!", 3)
print("Encrypted:", encrypted)  # Encrypted: Khoor, Zruog!

decrypted = caesar_cipher(encrypted, 3, mode='decrypt')
print("Decrypted:", decrypted)  # Decrypted: Hello, World!
