# Name; Alyssa Kelley
# Lab 0 - Week 1
# Date: 1/9/19
# Using Python 2.7.10

from sys import argv

def main(argv):
	file_name = argv[1]
	with open(file_name, 'r') as file_object:
		numProblems = file_object.readline()
		for line in file_object:
			a, b = (line.strip().split(' '))
			the_gcd = gcd(int(a), int(b))
			the_lcm = lcm(int(a), int(b))
			print("{} {}".format(the_gcd, the_lcm))

def gcd(a, b):
# Find the greatest common divisor of a and b
# Hint: Use Euclid's Algorithm
# https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
	if (b == 0):
		return a
	else:
		return gcd(b, a%b)
	#print ("gcd of {} and {}".format(a, b))

def lcm(a, b):
# Find the least common multiple of a and b
# Hint: Use the gcd of a and b
	lcm = (a*b)//gcd(a,b)
	#print("lcm of {} and {}".format(a, b))
	return lcm

if __name__ == "__main__":
	main(argv)