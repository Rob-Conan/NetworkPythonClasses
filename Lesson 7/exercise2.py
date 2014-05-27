# Use regular expressions to find all
# remote hostnames, remote IP addresses,
# and remote plaftforms
import re

remote_hosts = []
IPs = []
platform = []

with open("sw1_cdp.txt", 'r') as f:
	for line in f:
		hosts = re.search(r"Device ID: (.+)", line)
		if hosts:
			if not hosts.group(1) in remote_hosts:
				remote_hosts.append(hosts.group(1))
		ips = re.search(r"IP address: (.+)", line)
		if ips:
			if not ips.group(1) in IPs:
				IPs.append(ips.group(1))
		plat = re.search(r"Platform: (.+?) (.+?),", line)
		if plat:
			 remote_platform = plat.group(1) + " " + plat.group(2)
			 platform.append(remote_platform)
			

	print  remote_hosts
	print  IPs
	print platform