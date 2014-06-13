import ipaddress

class IPAddressWithNetmask(ipaddress.IPAddress):
	def __init__(self, IP):
		ipaddress.IPAddress.__init__(self, IP.split('/')[0])
		self.netmask = IP.split('/')[1]