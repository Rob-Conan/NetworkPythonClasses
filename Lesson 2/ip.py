import math

a = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

list_a = a.split()

list_b = list_a[1]
list_c = list_a[4:-1]

print "%-20s %-20s" % ('ip_prefix', 'as_path')
print "%-20s %-20s" % (list_b, list_c)