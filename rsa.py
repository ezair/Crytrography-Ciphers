'''
Author:	Eric Zair
File:	rsa.py
Description:	The purpose of this program was to create my own python2 implementation of
				the RSA encryption algorithm.
				In this file you will find a class named "RSA". This class takes
				care of all the encryption and decryption.
				When this program runs, it will ask the user to either:
					1) Encrypt something
					2) Decrypt something

				Note:
					DO NOT use this encryption system in real practice,
					as there are many other tested and proven to be secure
					algorithms out there for practical use.
'''
import random

class RSA:

	#Default Constructor
	def __init__(self):
		pass


	#checks to see if a number is prime
	#Return type: boolean
	def isprime(self, num):
		for i in range(200):
			rand = random.randint(2, num-1)
		return pow(rand, num-1, num) != 1


	#Generate big random primes.
	#Return integers: p, q, n, and phi
	def generateRandomPrimes(self, bit_length):
		p = random.getrandbits(bit_length) | 2^(bit_length) | 1
		while not self.isprime(p):
			p = random.getrandbits(bit_length) | 2^(bit_length) | 1

		q = random.getrandbits(bit_length) | 2^(bit_length) | 1
		while not self.isprime(q):
			q = random.getrandbits(bit_length) | 2^(bit_length) | 1
		
		#set n and phi.
		n = p*q
		phi = (p-1) * (q-1)
		return p, q, n, phi


	#Extended Euclidian Algorithm
	#Gcd(p,q) == ax + by
	#Gives you the private key.
	#gives the greatest common divisor
	#return x1 (the value of d)
	def extendedEgcd(self, a, b):
		phi = b
		x1, x2 = 1, 0
		y1, y2 = 0, 1
		while b:
			q = a // b
			x2, x1 = (x1 - q*x2), x2
			y2, y1 = (y1 - q*y2), y2
			a, b = b, (a - q*b)
		if x1 < 0:
			x1 += phi
		return x1


	#get the value of our random generated e.
	def setE(self,phi, bit_length):	
		#calculate the gcd of two numbers.
		def gcd(a,b):
			while b:
				a,b = b, a%b
			return a
		
		#make sure that e is a long number
		low_limit = 1 << bit_length-1
		low_limit -= 1
		
		potential_e = random.randint(low_limit, phi-1)
		potential_e = potential_e | 1

		while gcd(potential_e, phi) != 1:
			potential_e = random.randint(low_limit, phi-1)
			potential_e = potential_e | 1
		
		return potential_e


	#Encrypt the all the text in a given file.
	def encrypt(self, plaintext_filename, encryptedtext_filename, bit_length):
		print("Encrypting...")

		p, q, n, phi = self.generateRandomPrimes(bit_length)
		#set the value of e.
		e = self.setE(phi, bit_length)
		d = self.extendedEgcd(e, phi)

		#Create files to store read and write to.
		plaintext_file = open(plaintext_filename, 'r')
		encryptedtext_file = open(encryptedtext_filename, 'w')
		key_file = open("EncryptionKeys.txt", 'w')
		
		#write keys to encrypted file.
		key_file.write("d = " + str(d) + "\n\n")
		key_file.write("e = " + str(e) + "\n\n")
		key_file.write("n = " + str(n) + "\n\n")

		#read each character in the plaintext file.
		#Encrypt each letter individually and then write it to the encrypted filename.
		for line in plaintext_file:
			for character in line:
				encrypted_character = pow(ord(character), e, n)
				encryptedtext_file.write(str(encrypted_character) + '\n')
		
		print("Encryption complete.")
		key_file.close()
		encryptedtext_file.close()
		plaintext_file.close()


	#Decrypt a given rsa file with the proper private key.
	#Parameters: encryptedtext_file (string: filename of the file you want to decrypt)
	#			 public_key(tuple:	(d, n))
	def decrypt(self, encryptedtext_filename, decrypted_filename, public_key):
		print("Running decryption")

		encryptedtext_file = open(encryptedtext_filename, 'r')
		decrypted_file = open(decrypted_filename, 'w')

		for c in encryptedtext_file:
			m = pow(int(c), public_key[0], public_key[1])
			decrypted_file.write(chr(m))
		
		print("Decryption complete.")
		encryptedtext_file.close()
		decrypted_file.close()

#_______________________________________________________________________________________
#Build implemented rsa object
rsa = RSA()

#decrypt
def decrypt():
	private_key = (int(raw_input("Enter d (just copy and paste it from encryptedKeyfile): ")), int(raw_input("Enter n (just copy and paste it encryptedKey file): ")))
	encryptedtext_filename = raw_input("Enter the name of the encrypted text file: ")
	decrypted_filename = raw_input("Enter the name of the file you would like to write the decryption to: ")
	rsa.decrypt(encryptedtext_filename, decrypted_filename, private_key)


def main():
	option = int(raw_input("1) Encrypt\n2) Decrypt\nEnter one of the above options: "))

	#encrypt
	if option == 1:
		rsa.encrypt(raw_input("Enter the plaintext filename: "), raw_input("Enter the ciphertext filename: "), int(raw_input("Enter the bit_length: ")))
	#decrypt
	else:
		decrypt()

#call main method
if __name__=="__main__":
	main()