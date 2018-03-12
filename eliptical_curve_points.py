'''
Author:	Eric Zair
File:	eliptical_curve_points.py
Descriptions:	Calculates all the points
				of an eliptical curve
				of given a, b, and p values.
'''
from math import sqrt


#calculate and print out all modular inverses.
def calculate(a, b, p):
	for x in range(p):
		y2 = (x**3 + b % p) % p
		print "X:", x
		print "y2 = a mod p:", y2

		num = y2**((p-1)/2) % p
		if num == 1:
			print "a^(p-1)/2:", 1
			y = y2**((p+1)/4) % p
			print "y:", y, "and", -y
		else:
			print "a^(p-1)/2:", -1		
		print "\n"


def main():
	a = int(raw_input("Enter A value: "))
	b = int(raw_input("Enter B value: "))
	p = int(raw_input("Enter P value: "))
	calculate(a, b, p)

if __name__=="__main__":
	main()