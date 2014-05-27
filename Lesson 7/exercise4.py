# Expand on 3 to work for more data


import re
import pprint
data ={}

with open("ospf_data.txt") as f:
	for line in f:
		Int = re.search(r"(.+?) is up,", line)
		if Int:
			interface = Int.group(1)
			data[interface] = {}
		IP = re.search(r"Internet Address (.+?), Area (.+?),", line)
		if IP:
			data[interface]['IP address'] = IP.group(1)
			data[interface]['Area'] = IP.group(2)
		Ty = re.search(r"Network Type (.+?), Cost: (.+)", line)
		if Ty:
			data[interface]['Type'] = Ty.group(1)
			data[interface]['Cost'] = Ty.group(2)
		hey = re.search(r"Hello (.+?), Dead (.+?),", line)
		if hey:
			data[interface]['Hello'] = hey.group(1)
			data[interface]['Dead'] = hey.group(2)
pprint.pprint(data)