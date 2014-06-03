import re

def obtain_uptime(file_read):
    lines = file_read.split('\n')
    for line in lines:
    	var = re.search(r"uptime is (.+)", line)
    	if var:
    		return var.group(1)