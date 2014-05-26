# Function to carry out binary conversion of an IP address
# Based on Lecture 3 exercise 1

import math


def BinaryConversion(ip_addr):
	octets = ip_addr.split('.')
	
	if len(octets) != 4:						# Some crude error checking
		sys.exit("Please enter a valid IP address")

	a = range(4)							# Create a list of [0,1,2,3]
	b = a[0:]							# Create a copy of the original list
	for i,enum in enumerate(octets):
		a[i] = bin(int(enum))					# Change list to be the binary of our input
#		print a[i]						# Print for debugging purposes
		b[i] = a[i][2:]						# Remove the first two "bytes" (0b)
		while len(b[i]) <= 8:
			b[i] = '0' + b[i]
#		print b[i];						# Print for debugging purposes

	bin_addr = ".".join(b)
	return bin_addr
