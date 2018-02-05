'''
Author:	Eric Zair
File:	Affine.py
Description:	Contains a class file for using an affine
				encryption and decryption.
'''


class AffineCipher():

	#class variables
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


	#Default Constructor
	def __init__(self):
		#this object will not be passed any instance variables.
		pass


	'''
	Return a list of intergers corresponding to it's location in the alphabet.
	parameters:	plain_text (String: message that the used wants to encrypt/decrypt)
	return type:	list of integers
	'''
	def plainTextToNumbers(self, plain_text):
		plain_text = plain_text.upper()
		plain_text_to_numbers = []
		#insert the number that represents each letter in the plain_text into a list.
		for letter in plain_text:
			plain_text_to_numbers.append(self.alphabet.index(letter))
		return plain_text_to_numbers


	'''
	Converts the list of numbers back to a string.
	parameters:	numbers (list of integers: numbers from the original string the user gave)
	return type:	string
	'''
	def numbersToPlainText(self, list_of_numbers):
		numbers_to_plain_text = ""
		for number in list_of_numbers:
			numbers_to_plain_text += self.alphabet[number]
		return numbers_to_plain_text


	'''
	Returns the encrypted plain_text.
	parameters:	a (integer: part 1 of the encryption key)
				b (integer:	part 2 of the encryption key)
				plain_text (string: the message the user wants to encrypt)
	'''
	def encrypt(self, plain_text, a, b):
		#convert the plain text to a list of numbers.
		plain_text_to_numbers = self.plainTextToNumbers(plain_text)

		encrypted_plain_text_to_numbers = []
		#encrypt the the text
		for number in plain_text_to_numbers:
			encrypted_plain_text_to_numbers.append( (a*number + b) % len(self.alphabet) )

		#convert the list of numbers back into a string in the form of the encrypted message and return it.
		return self.numbersToPlainText(encrypted_plain_text_to_numbers)


	'''
	Returns the decrypted plain_text.
	parameters:	encrypted_plain_text (string: message that the user has already encrypted)
				a (integer: part 1 of the encryption key)
				b (integer:	part 2 of the encryption key)
	return type: string
	'''
	def decrypt(self, encrypted_plain_text, a, b):
		#convert encrypted_plain_text back into a list of integers.
		encrypted_plain_text_to_numbers = self.plainTextToNumbers(encrypted_plain_text)

		#Calculate a inverse (aka c)
		c = 0
		for i in range(len(self.alphabet)):
			if (a*i % len(self.alphabet)) == 1:
				c = i
				break

		#begin the decryption process
		decrypted_plain_text_to_number = []
		for number in encrypted_plain_text_to_numbers:
			decrypted_plain_text_to_number.append( (c*(number-b)) % len(self.alphabet) )
		
		#convert the decrypted list of numbers back into a string and return it
		return self.numbersToPlainText(decrypted_plain_text_to_number)
