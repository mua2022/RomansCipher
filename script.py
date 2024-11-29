def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Non-alphabetic characters are not changed
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher Tool!")
    text = input("Enter the text: ")
    while True:
        try:
            shift = int(input("Enter the shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for the shift value.")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return
    
    result = caesar_cipher(text, shift, mode)
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
