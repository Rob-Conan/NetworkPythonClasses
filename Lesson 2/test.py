import math

ip_address = raw_input("Please enter an IP address: ")

print "The IP address now is: %s" % ip_address

list_a = ip_address.split('.')

if (len(list_a) == 3):
	list_a.append('0')
elif (len(list_a) == 4):
	list_a[3] = '0'

print "%-20s %-20s %-20s" % ('Network Number', 'First Octet Binary', 'First Octet Hex')
print "%-20s %-20s %-20s" % ('.'.join(list_a), bin(int(list_a[0])), hex(int(list_a[0])))

ip_addr = raw_input("Please enter another IP address: ")

list_b = ip_addr.split('.')

print "%-20s %-20s %-20s %-20s" % ('First', 'Second', 'Third', 'Fourth')
print "%-20s %-20s %-20s %-20s" % (bin(int(list_b[0])), bin(int(list_b[1])), bin(int(list_b[2])), bin(int(list_b[3])))