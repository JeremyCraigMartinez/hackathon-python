#!/usr/bin/python3

from ip_lookup import ip_lookup, button_lookup
import sys
import json
import urllib.request
import websocket
import ssl
import socket

from csvfile import *

if __name__ == "__main__":
	count = 0
	hits = []
	for contents in parse(sys.argv[1]):
		count = count + 1
		if count > 10000:
			print(hits)
			sys.exit()
		list_of_everything = []
		if len(sys.argv) > 1:
			for each in contents:
				obj = make_JSON(contents)	
			for each_ip in obj:	
				if not each_ip.startswith("134"):
					domain = ip_lookup(each_ip)
					button = button_lookup(domain)
					if domain != None:
						hits = hits + [{'domain':domain,'button':button}]
						list_of_everything = list_of_everything + [{'domain':domain,'button':button}]
		else:
			print("Enter file...")

		url = 'http://104.236.169.12:5024/hello'
		for each in list_of_everything:
			params = json.dumps(each).encode('utf8')

			req = urllib.request.Request(url, data=params, headers={'content-type':'application/json'})
			response = urllib.request.urlopen(req)
