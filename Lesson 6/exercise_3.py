# Based on Lesson 4's IP validator
# validate an IP (given as a function input)
# Return true or false

import sys
import math

valid = False

def validateIP(ip_addr):
	octects = ip_addr.split('.')
	if len(octects) != 4:
			valid = False
	else:
		if int(octects[0]) == 127 or int(octects[0]) < 1 or int(octects[0]) > 223:
			valid = False
		else:
			if int(octects[0]) == 169 and int(octects[1]) == 254:
				valid = False
			for i in (int(octects[1]), int(octects[2]), int(octects[3])):
				if 0 <= i <= 255:
					valid = True
				else:
					valid = False
					break
	return valid