# Uptime class to parse an uptime string

import sys
import re

class Uptime(object):
	def __init__ (self, uptime):
		self.uptime = uptime
		self.getUptime()

	def getUptime(self):
		years = re.search(r"(.+) (.+?) years,", self.uptime)
		if years:
			self.years = years.group(2)
		else:
			self.years = 0
		weeks = re.search(r"(.+) (.+?) weeks,", self.uptime)
		if weeks:
			self.weeks = weeks.group(2)
		else:
			self.weeks = 0
		days = re.search(r"(.+) (.+?) days,", self.uptime)
		if days:
			self.days = days.group(2)
		else:
			self.days = 0
		hours = re.search(r"(.+) (.+?) hours,", self.uptime)
		if hours:
			self.hours = hours.group(2)
		else:
			hours = re.search(r"(.+) (.+?) hour,", self.uptime)
			if hours:
				self.hours = hours.group(2)
			else:
				self.hours = 0
		minutes = re.search(r"(.+) (.+?) minutes", self.uptime)
		if minutes:
			self.minutes = minutes.group(2)
		else:
			self.minutes = 0

	def uptime_seconds(self):
		self.seconds = int(self.years) * 365 * 24 * 60 * 60 + int(self.weeks) * 7 * 24 * 60 * 60
		self.seconds += int(self.days) * 24 * 60 * 60 + int(self.hours) * 60 * 60
		self.seconds += int(self.minutes) * 60
		return self.seconds