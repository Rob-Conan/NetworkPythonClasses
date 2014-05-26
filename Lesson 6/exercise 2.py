# Function to convert a list to a dictionary
# Where list index is dictionary key

def ListToDict(list_a):
	new_dict = {}
	print list_a
	for i,k in enumerate(list_a):
		new_dict[i] = k
	return new_dict


a = range(10)
b = ListToDict(a)
print a
print b