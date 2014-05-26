# Use exercise 3 and 4 to check if an IP is valid
# before converting to binary

from exercise_3 import validateIP
from exercise_4 import BinaryConversion
import sys

if not len(sys.argv) == 2:
	sys.exit("Please provide an IP address")
else:
	ip_addr = sys.argv[1]
	valid = validateIP(ip_addr)
	if valid == True:
		binary = BinaryConversion(ip_addr)
		print "%-20s %-20s" % ("IP Address", "Binary Address")
		print "%-20s %-20s" % (ip_addr, binary)