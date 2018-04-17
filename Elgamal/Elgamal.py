'''
Author:	Eric Zair
File:	Elgamal.py
Description:	This file contains the Decryption
				for Elgamal public key encryption.

				Note:
					This file will be used as an API
					for an encrypted chat program.
'''
import random


'''
Returns the modular inverse of a number.
Parameters: int a(the number you want the inverse of)
			int b(your prime p value)
Return type: int
'''
def extendedEgcd(a, b):
	original_b = b
	x1, x2 = 1, 0
	y1, y2 = 0, 1
	while b:
		q = a//b
		x2, x1 = (x1 - q*x2), x2
		y2, y1 = (y1 - q*y2), y2
		a, b = b, (a - q*b)
	if x1 < 0:
		x1 += original_b
	return x1


#checks to see if a number is prime
#parameters: int num(the number you want to check if prime)
#Return type: boolean
def isprime(num):
	for i in range(200):
		rand = random.randint(2, num-1)
	return pow(rand, num-1, num) != 1


#Generate big random prime numbers
#Return integers: p
def generateRandomPrime(bit_length):
	p = random.getrandbits(bit_length) | 2^(bit_length) | 1
	while not isprime(p):
		p = random.getrandbits(bit_length) | 2^(bit_length) | 1
	return p

#Generates the random private keys a and b
#return type: int
def generatePrivateKey(bit_length):
	return random.getrandbits(bit_length)


#Returns a Generator g
#return type: int
def generateGenerator(p):
	q = (p-1)/2
	g = random.randint(2, q-1)
	condition1 = pow(g, 1, p) ==  1 % p
	condition2 = pow(g, 2, p) == 1 % p
	condition3 = pow(g, q, p) == 1 % p
	while condition1 or condition2 or condition3:
		g = random.randint(2, q-1)
	return g


#Encrypt any give file.
#parameters: string filename(name of the file you want to decrypt)
#return type: void
def encrypt(filename):
	p = generateRandomPrime(1100)
	a = generatePrivateKey(1100)
	b = generatePrivateKey(1100)
	g = generateGenerator(p)
	alice_public_key = pow(g, a, p)
	bob_public_key = pow(g, b, p)
	private_key = pow(g, a*b, p)

	#file the encryption is being logged to
	encrypted_file = open(filename + ".encrypt", 'w')
	
	#file the keys are being logged to 
	key_file = open(filename + ".keys", 'w')
	key_file.write("p = " + str(p))
	key_file.write("\n\na = " + str(a))
	key_file.write("\n\nb = " + str(b))
	key_file.write("\n\ng = " + str(g))
	key_file.write("\n\nalice_public_key = " + str(alice_public_key))
	key_file.write("\n\nbob_public_key = " + str(bob_public_key))
	key_file.write("\n\ng^(ab) = " + str(private_key))
	
	#Write to the encrypted file.
	with open(filename, 'r') as file:
		for plain_text in file:
			for m in plain_text:
				encrypted_file.write(str(ord(m) * private_key) + "\n")


#Decrypt a the content in any given file.
#parameters:
#			int p (value all keys are modded off of)
#			int key (the private key, g^ab)			
#			string filename (name of the file you are decrypting)
#return type: void
def decrypt(filename, key, p):
	decrypted_filename = filename[0 : filename.index('.txt')] + ".txt.decrypt"
	decrypt_file = open(decrypted_filename, 'w')
	with open(filename, 'r') as file:
		for c in file:
			m = int(c) * extendedEgcd(key, p) % p
			decrypt_file.write(chr(m))


#___________________________________________________________________________________
def main():
	option = int(raw_input("(1)Encrypt\n(2)Decrypt\nSelect an option: "))

	#encryption
	if option == 1:
		filename = raw_input("Enter the name of the file you want to encrypt: ")
		print("Encrypting...")
		encrypt(filename)

	#decryption
	elif option == 2:
		filename = raw_input("Enter the name of the file you want to decrypt: ")
		p = int(raw_input("Enter p: "))
		key = int(raw_input("Enter g^(ab): "))
		print("Decrypting...")
		decrypt(filename, key, p)

	#there is an error
	else:
		print "Error not a valid option!\nPlease Re-run program."

if __name__=='__main__':
	main()