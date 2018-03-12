'''
Author:	Eric Zair
File:	eliptical_curve_points.py
Descriptions:	Calculates all the points
				of an eliptical curve
				of given a, b, and p values.
'''


#Calculate number inverses.
def extendedEgcd(a, b):
	hold_b = b
	x1, x2 = 1, 0
	y1, y2 = 0, 1
	while b:
		q = a//b
		x2, x1 = (x1 - q*x2), x2
		y2, y1 = (y1 - q*y2), y2
		a, b = b, (a - q*b)
	if x1 < 0:
		x1 += hold_b
	return x1


#calculate and print out all modular inverses.
#returns a list of points.
def calculate(a, b, p):
	points = []
	for x in range(p):
		y2 = (x**3+ a*x + b) % p
		print "X:", x
		print "y2 = a mod p:", y2

		num = (y2**((p-1)/2)) % p
		if num == 1:
			print "a^(p-1)/2:", 1
			y = y2**((p+1)/4) % p
			points.append(tuple((x, y)))
			points.append(tuple((x, p-y)))
			print "y:", y, "and", -y	
		else:	
			print "a^(p-1)/2:", -1
		
		print "\n"
	print "P + P = " + str(extendedEgcd(y2, p))	
	return points

#Print out the list of points given as a parameter.
def printPoints(points):
	print "Points:"
	print "print number of points:", len(points)
	for point in points:
		print "\t", point

	#for i in range (len(points)-1):
	#	print "\t(" + str(points[i][0]) + ", " + str(points[i+1][0]) + ")"

def main():
	a = int(raw_input("Enter A value: "))
	b = int(raw_input("Enter B value: "))
	r = int(raw_input("Enter R value: "))
	print ""
	printPoints(calculate(a,b,r))

if __name__=="__main__":
	main()