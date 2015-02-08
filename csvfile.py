#!/usr/bin/python3

import csv
import os
import sys
import re

regex_lookup = { #number at the beginning of the key is for sorted purposes
	'ip_address' : '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d+)?',
}	

order = ['ip_address']

def parse(f):
	with open(f) as log:
		for line in log:
			yield line

def make_JSON(contents):
	arr = []
	for header in order:
		for string in re.finditer(regex_lookup[header],contents):
			s = string.group().strip()
			try: 
				arr = arr + [s[:s.index("/")]]
			except: arr = arr + [s]
	return arr

if __name__ == '__main__':
	for each in parse(sys.argv[1]):
		obj = make_JSON(contents)