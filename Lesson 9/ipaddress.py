#Python class to represent an IP address.

import sys
import math

#A. Display the IP address in Binary

class IPAddress(object):
	def __init__ (self, IP):
		self.ip_addr = IP
		self._octets = IP.split('.')

# Method code from Lesson 6 Exercise 4
	def display_in_binary(self):
		if self.is_valid() == False:
			sys.exit("IP address not valid")

		a = range(4)
		b = a[0:]

		for i,enum in enumerate(self._octets):
			a[i] = bin(int(enum))
			b[i] = a[i][2:]
			while len(b[i]) <= 8:
				b[i] = '0' + b[i]

		self.bin_addr = ".".join(b)
		return self.bin_addr

# New method to display in Hex
	def display_in_hex(self):
		if self.is_valid() == False:
			sys.exit("IP address not valid")

		a = range(4)
		b = a[0:]

		for i,enum in enumerate(self._octets):
			a[i] = hex(int(enum))
			b[i] = a[i][2:]
			while len(b[i]) < 2:
				b[i] = '0' + b[i]

		self.hex_addr = ".".join(b)
		return self.hex_addr


# Method code from Lesson 8 Exercise 1
	def is_valid(self):
		valid = False
		if len(self._octets) != 4:
			valid = False
		else:
			try:
				if int(self._octets[0]) == 127 or int(self._octets[0]) < 1 or int(self._octets[0]) > 223:
					valid = False
				else:
					if int(self._octets[0]) == 169 and int(self._octets[1]) == 254:
						valid = False
					else:
						for i in (int(self._octets[1]), int(self._octets[2]), int(self._octets[3])):
							if 0 <= i <= 255:
								valid = True
							else:
								valid = False
								break
			except ValueError:
				pass
		return valid
