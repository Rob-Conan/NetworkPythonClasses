# Use regular expressions to extract remote hostname,
# IP address, mode, vendor, and device_type


import re
device ={}

with open('r1_cdp.txt', 'r') as f:
	for line in f:
		# Hostname = Device ID: SW1 
		# IP Address = IP address: 10.1.1.22
		# Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
		# Model = WS-C2950-24
		# Vendor = cisco
		# Device Type = Switch
		a = re.search(r"Device ID: (.+)", line)
		if a:
			hostname = a.group(1)
			print hostname
		b = re.search(r"IP address: (.+)", line)
		if b:
			ip_addr = b.group(1)
			print ip_addr
		c = re.search(r"Platform: (.+?) (.+?),  Capabilities: (.+?) ", line)
		if c:
			vendor = c.group(1)
			model = c.group(2)
			device_type = c.group(3)
	device['hostname'] = hostname
	device['ip_addr'] = ip_addr
	device['vendor'] = vendor
	device['model'] = model
	device['device_type'] = device_type

print device