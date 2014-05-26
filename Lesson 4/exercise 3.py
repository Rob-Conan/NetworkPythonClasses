# Convert uptimes to seconds

### CODE IS WRONG - valid = entry.split is wrong
### Too Late, will redo tomorrow

import math
import pprint

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

items = {}
for uptime in (uptime1, uptime2, uptime3, uptime4):
	total_uptime = 0
	device = uptime.split(' ')
	device_name = device[0]
	uptime_value = uptime.split(',')
	for entry in uptime_value:
		if 'uptime is' in entry:
			entry = entry.split()[3:]
		else:
			entry = entry.split()
		try:
			if 'years' in entry[1]:
				total_uptime += int(entry[0]) * 365 * 24 * 60 * 60
			elif 'weeks' in entry[1]:
				total_uptime += int(entry[0]) * 7 * 24 * 60 * 60
			elif 'days' in entry[1]:
				total_uptime += int(entry[0]) * 24 * 60 * 60
			elif 'hour' in entry[1]:
				total_uptime += int(entry[0]) * 60 * 60
			elif 'minutes' in entry[1]:
				total_uptime += int(entry[0]) * 60
		except ValueError:													# Catch bad conversion of string to int
			pass

	items[device_name] = total_uptime

pprint.pprint(items)