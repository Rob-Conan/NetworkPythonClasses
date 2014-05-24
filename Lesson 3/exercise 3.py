# Parsing "show ip int brief" output
# Create a list where each element in the list is a tuple consisting of
# (interface_name, ip_address, status,. protocol)
# Only add interfaces that are in the up/up state

import math

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10         YES     NVRAM       up          up
NVI0                  6.9.4.10        YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

print len(show_ip_int_brief)
print show_ip_int_brief

input_list = show_ip_int_brief.split('\n')
input_row = []
print "%-20s %-20s %-20s %-20s" % ("Interface", "IP Address", "Status", "Protocol")
for val in input_list:
	j = val.split()									#Remove spaces between entries
	if "Interface" in val or len(j) != 6:			#Ignore lines that are too short and that contain "Interface"
		continue
	if j[4] == 'up' and j[5] == 'up':				# Print if Status = Protocol = Up	
		print "%-20s %-20s %-20s %-20s" % (j[0], j[1], j[4], j[5])



	
	
