'''
Eric Zair
Hw 3
Cryptography
Dr.Gurajala

Description: This program calculates the squares
			 of a given p, q, and n value
'''


#calulate the lengendre of any given number.
#returns an integer.
def legendre(number, mod_value):
	if pow(number, (mod_value-1)/2, mod_value) == 1:
		return 1
	else:
		return -1


#just prints out squares and pseudo squres.
def printSquares(pseudo_squares, squares, non_squares):
	print "QR Squares:"
	for square in squares:
		print square
	
	print "\nPsuedo Squares:"
	for pseudo_square in pseudo_squares:
		print pseudo_square

	print "\nNQR squares"
	for non_square in non_squares:
		print non_square

#_______________________________________________
def main():
	QRs = []
	NQRs = []
	pseudo_squares = []
	#our values.
	p = int(raw_input("Enter a p value: "))
	q = int(raw_input("Enter a q value: "))
	n = p*q

	for x in range(1, n):
		q_legendre = legendre(x, q)
		p_legendre = legendre(x, p)
		n_legendre = q_legendre * p_legendre
		print "x:", x
		print "x/q:", q_legendre
		print "x/p:", p_legendre
		print "x/n:", n_legendre, "\n"
		
		if x%p != 0 and x%q != 0: 
			if n_legendre == 1 and p_legendre == -1 and q_legendre == -1:
				pseudo_squares.append(x)				
			elif n_legendre == 1 and p_legendre == 1 and q_legendre == 1:
				QRs.append(x)
			
			if x not in QRs:
				NQRs.append(x)

	printSquares(pseudo_squares, QRs, NQRs)

if __name__=="__main__":
		main()