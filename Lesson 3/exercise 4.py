# Create a script that checks the validity of an IP address
# Checks
# - Four Octets
# - Octet 1 between 1 - 223
# - First Octet != 127
# - IP address can not be in 169.254.X.X address space
# - Last three octects range from 0 - 255

import sys

valid = True

if len(sys.argv) != 2:
	sys.exit("Please enter a (single) IP address")
else:
	octects = sys.argv[1].split('.')
	if len(octects) != 4:
		valid = False
	else:
		if octects[0] == '127' or octects[0] < '1' or octects[0] > '223':
			valid = False
		else:
			if octects[0] == '169' and octects[1] == '254':
				valid = False
			for i in (octects[1], octects[2], octects[3]):
				if 0 <= i <= 255:
					valid = True

if valid == True:
	print sys.argv[1] + " is Valid"
else:
	print sys.argv[1] + " is Not Valid"
					
