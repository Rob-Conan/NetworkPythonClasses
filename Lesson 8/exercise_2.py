"""Create three functions in three separate modules and put them in a show_version directory (in practice you wouldn't do this--you would just have them all in one file, but this will let you experiment with packages).
            1. Function1 = obtain_os_version -- process the show version output and return the OS version (Version 15.0(1)M4) else return None.
            2. Function2 = obtain_uptime -- process the show version output and return the network device's uptime string (uptime is 12 weeks, 5 days, 1 hour, 4 minutes) else return None.
            3. Function3 = obtain_model -- process the show version output and return the model (881) else return None.

    B. Make a package out of this 'show_version' directory using a blank __init__.py file.
"""
import show_version


with open ("show_version.txt") as f:
	lines = f.read()
	print "Version: %s" % show_version.obtain_os_version(lines)
	print "Model: %s" % show_version.obtain_model(lines)
	print "Uptime: %s" % show_version.obtain_uptime(lines)