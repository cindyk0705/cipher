# cipher
> *This program was originally written for the MSCI 121 course at the University of Waterloo, taught by Mark Smucker. The included features were written to match the requirements of the assignment.*

A simple letter-to-letter mapping encryption and decryption program. 

### Explanation
The program reads a .txt file with 4 lines:

```
.txt file with the encryption key
the command "encrypt" or "decrypt"
.txt file with the text to encrypt/decrypt
.txt file to store the results
```

Key must compose of all capital letters. Symbols, and letters not included in the key (if the key is shorter than 26 letters) are not affected.
