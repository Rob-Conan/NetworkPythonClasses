import re

def obtain_model(file_input):
	lines = file_input.split('\n')
	for line in lines:
		if 'bytes of memory' in line:
			var = re.search(r"(.+) (.+?) processor ", line)
			if var:
				return var.group(1)