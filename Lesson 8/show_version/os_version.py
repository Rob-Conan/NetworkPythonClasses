import re

def obtain_os_version(file_read):
	lines = file_read.split('\n')
	for line in lines:
		version = re.search(r"Cisco IOS Software, (.+?), (.+?),", line)
		if version:
			return version.group(2)