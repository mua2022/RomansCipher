# RomansCipher
Caesar cipher encryption and decryption python script

# Caesar Cipher Tool - How It Works

## Encrypt/Decrypt Logic
- For **encryption**, the script shifts the letters forward by the given shift value.
- For **decryption**, it reverses the shift by using `-shift`.

---

## Input Handling
1. **Text**: Any string input provided by the user.
2. **Shift**: An integer value defining the number of positions to shift the alphabet.
3. **Mode**: The user selects either `encrypt` or `decrypt`.

---

## Alphabet Handling
- Uppercase and lowercase letters are kept distinct.
- Non-alphabetic characters (like spaces, punctuation, or numbers) remain unchanged.

---

### Example Workflow:
1. **Encrypting**:
   - Input Text: `Hello, World!`
   - Shift: `3`
   - Output: `Khoor, Zruog!`

2. **Decrypting**:
   - Input Text: `Khoor, Zruog!`
   - Shift: `3`
   - Output: `Hello, World!`

This ensures that the cipher respects the case of letters while maintaining the integrity of non-alphabetic characters.

Out of my zeal and passion in cyber security i started to come up with a script to help me solve cryptography challenges in CTF environment.    
                                         | MUA |  
                                         
     ~  A man grows  from the mistakes and challenges they come across. Alas! Happy decrypting the Romans cipher~
     
