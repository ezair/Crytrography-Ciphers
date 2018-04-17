When you run Elgamal.py is prompts you for two options
1) Encryption
2) Decryption


__ENCRYPTION__
If you enter 1 for encryption, you are prompted for the filename of the file you would like to encrypt(as a string)
After the encryption runs, it generates two files.
These two files a nameOfFile.encrypt and nameOfFile.keys
nameOfFile.encrypt is the encrypted file.
nameOfFile.keys contains ALL of the keys you will need and ever will need to decrypt nameOfFile.encrypt


__DECRYPTION__
If you enter 2 for Decryption, you are promted to enter the name of the file you want to decrypt(as a string),
the prime P, and the private key g^(ab).
All of the these keys are located in the nameOfFile.keys file.
Copy them and paste them for decryption.
The decrypted file will be called nameOfFile.decrypt
It's as simple as that.


__NOTE__:
  The format of the encrypted file is just every single character encrypted individually and on their own seperate line.
