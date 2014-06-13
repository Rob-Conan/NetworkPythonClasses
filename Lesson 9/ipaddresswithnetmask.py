import ipaddress
import math

class IPAddressWithNetmask(ipaddress.IPAddress):
	def __init__(self, IP):
		ipaddress.IPAddress.__init__(self, IP.split('/')[0])
		self.netmask = IP.split('/')[1]

	def netmask_in_dotdecimal(self):
		whole = int(self.netmask) / 8
		remainder = int(self.netmask) % 8
		net = []
		# Account for any complete bytes
		for i in xrange(whole):
			net.append('11111111')
		
		# Account for all 1's in an 'incomplete' byte
		last = '1'
		c = 0
		while c < remainder - 1:
			last += '1'
			c += 1

		end = 8 - remainder

		# Append the incomplete byte with 0's
		if end < 8:
			while end > 0:
				last += '0'
				end -= 1
			net.append(last)

		# Append complete 0 bytes to reach the four byte size (for IPv4) 
		while len(net) < 4:
			net.append('00000000')

		return '.'.join(net)