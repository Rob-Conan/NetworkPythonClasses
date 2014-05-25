# Based on Lesson 3's IP validator
# Request IP's until a valid address is found
# ------------------------------------------------------
# Create a script that checks the validity of an IP address
# Checks
# - Four Octets
# - Octet 1 between 1 - 223
# - First Octet != 127
# - IP address can not be in 169.254.X.X address space
# - Last three octects range from 0 - 255

import sys
import math

valid = False

if len(sys.argv) != 2:
	sys.exit("Please enter a (single) IP address")
else:
	new_input = sys.argv[1]
	octects = new_input.split('.')
	while valid == False:
		if len(octects) != 4:
			print "Octets wrong"
		else:
			if int(octects[0]) == 127 or int(octects[0]) < 1 or int(octects[0]) > 223:
				print "Octect 1 out of range"
			else:
				if int(octects[0]) == 169 and int(octects[1]) == 254:
					print "Invalid Range"
				for i in (int(octects[1]), int(octects[2]), int(octects[3])):
					if 0 <= i <= 255:
						valid = True
					else:
						valid = False
						break
		if valid == True:
			print new_input + " is Valid"
		else:
			print new_input + " is Not Valid"
			new_input = raw_input("Please enter a valid IP address: ")
			octects = new_input.split('.')


					
