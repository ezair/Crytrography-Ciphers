


class RSA:

	#Class data types.
	p = 0
	q = 0
	e = 0
	n = 0
	d = 0
	phi_n = 0


	#Constructor
	def __init__(self, p, q, e):
		#make sure p and q are positive
		if p < 0 or q < 0:
			raise ValueError('Error: P and Q must be positive numbers!.')

		#Make sure that e is odd.
		if e%2 == 0:
			raise ValueError('Error: E must be an odd number')

		#set all values.
		self.p = p
		self.q = q
		self.e = e
		self.n = p*q
		self.phi_n = (p-1) * (q-1)
		self.d = self.phi_n + self.extendedEgcd(self.e, self.phi_n)[1]


	#Euclidian Algorithm (gcd)
	def egcd(self, e, phi_n):
		#base case
		if phi_n == 0:
			return e
		else:
			return self.egcd(phi_n, e%phi_n)


	#Extended Euclidian Algorithm
	#Gcd(p,q) == ax + by
	#Gives you the private key.
	#gives the greatest common divisor
	def extendedEgcd(self, p, q):
		if p == 0:
			return (q, 0, 1)
		else:
			g, y, x = self.extendedEgcd(q%p, p)
			return (g, x - (q // p) * y, y)


	#return the private key
	def privateKey(self):
		return self.d, self.n


	#return the public key
	def publicKey(self):
		return self.e, self.n

#___________________________________________________________________________
rsa = RSA(11, 5, 7)
print rsa.publicKey()
print rsa.privateKey()
print rsa.test()