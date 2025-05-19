
def caesar_cipher(text, shift, mode='encrypt'):
    result = ''

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # Keep spaces and punctuation unchanged

    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Choose 'encrypt' or 'decrypt'.")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    result = caesar_cipher(text, shift, mode)
    print(f"\nResult ({mode}ed): {result}")

if __name__ == "__main__":
    main()
