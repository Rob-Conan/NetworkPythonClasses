import sys
import math



def validate(ip_addr):
	valid = False
	octects = ip_addr.split('.')
	if len(octects) != 4:
		valid = False
	else:
		try:
			if int(octects[0]) == 127 or int(octects[0]) < 1 or int(octects[0]) > 223:
				valid = False
			else:
				if int(octects[0]) == 169 and int(octects[1]) == 254:
					valid = False
				else:
					for i in (int(octects[1]), int(octects[2]), int(octects[3])):
						if 0 <= i <= 255:
							valid = True
						else:
							valid = False
							break
		except ValueError:
			pass
	return valid


if __name__ == '__main__':
	test_ip_addresses = {
        '192.168.1' : False,
        '10.1.1.' : False,
        '10.1.1.x' : False,
        '0.77.22.19' : False,
        '-1.88.99.17' : False,
        '241.17.17.9' : False,
        '127.0.0.1' : False,
        '169.254.1.9' : False,
        '192.256.7.7' : False,
        '192.168.-1.7' : False,
        '10.1.1.256' : False,
        '1.1.1.1' : True,
        '223.255.255.255': True,
        '223.0.0.0' : True,
        '10.200.255.1' : True,
        '192.168.17.1' : True,
    }
	for i,j in test_ip_addresses.items():
		res = validate(i)
		if res == j:
			print "Validated: %s as %s" % (i, j)
		else:
			print "Error validating %s" % i

