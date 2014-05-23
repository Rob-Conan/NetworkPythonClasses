# Lesson 3 Exercise 1
# Expanding from material learnt in Lesson 2
# - Create an IP address converter (dotted decimal to binary)
# 	1. Make the IP address a command-line argument
#	2. Simplify the script login using flow-control statements
#	3. Remove the 0b of the binary output and pad each output to be 8 digits
#	4. Print the standard output in both Decimal and Binary format
#


import sys

if len(sys.argv) == 2:
	ip_addr = sys.argv.pop()
	octets = ip_addr.split('.')
	
	if len(octets) != 4:					# Some crude error checking
		sys.exit("Please enter a valid IP address")

	a = range(4)							# Create a list of [0,1,2,3]
	b = a[0:]								# Create a copy of the original list
	for i,enum in enumerate(octets):
		a[i] = bin(int(enum))				# Change list to be the binary of our input
#		print a[i]							# Print for debugging purposes
		b[i] = a[i][2:]						# Remove the first two "bytes" (0b)
		while len(b[i]) <= 8:
			b[i] = '0' + b[i]
#		print b[i];							# Print for debugging purposes

	bin_addr = ".".join(b)
	print "%-20s %-20s" % ("IP Address", "Binary Address")
	print "%-20s %-20s" % (ip_addr, bin_addr)

elif len(sys.argv) > 2:
	print "Please enter one IP address"
else:
	print "Please enter an IP address"
