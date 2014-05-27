# Extract the Interface, IP address, area, type, cost, hello timer, and dead timer

import re

output = {}

with open("ospf_single_interface.txt") as f:
	for line in f:
		Int = re.search(r"(.+?) is up,", line)
		if Int:
			output['Interface'] = Int.group(1)
		IP = re.search(r"Internet Address (.+?), Area (.+?),", line)
		if IP:
			output['IP address'] = IP.group(1)
			output['Area'] = IP.group(2)
		Ty = re.search(r"Network Type (.+?), Cost: (.+)", line)
		if Ty:
			output['Type'] = Ty.group(1)
			output['Cost'] = Ty.group(2)
		hey = re.search(r"Hello (.+?), Dead (.+?),", line)
		if hey:
			output['Hello'] = hey.group(1)
			output['Dead'] = hey.group(2)

print output