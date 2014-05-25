# Parse the below string and store Vendor, Model, OS version, uptime, and serial number in a dictionary

import pprint

input = """Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102
"""

lines = input.split('\n')
items = {}

for line in lines:
	if 'Cisco IOS Software' in line:
		parts_a = line.split(',')
		items['vendor'] = parts_a[0]
		items['version'] = parts_a[2]
	elif 'uptime is' in line:
		parts_b = line.split(' ')
		items['uptime'] = ' '.join(parts_b[3:])
	elif 'Processor board ID' in line:
		parts_c = line.split(' ')
		items['serial_number'] = parts_c.pop()
	elif 'bytes of memory' in line:
		items['model'] = line

pprint.pprint(items)