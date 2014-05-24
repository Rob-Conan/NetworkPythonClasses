# Modify Lesson 2's IP.py script to use flow-control statements.


import math

a = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
b = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
c = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
d = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

print "%-20s %-20s" % ('ip_prefix', 'as_path')

for entry in (a, b, c, d):
	parsed = entry.split()
	ip_prefix = parsed[1]
	as_path = parsed[4:-1]
	print "%-20s %-20s" % (ip_prefix, as_path)