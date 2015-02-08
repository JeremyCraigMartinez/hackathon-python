import json
import ipaddress
import socket

from make_ips import write_ips

ips_object = write_ips()

def ip_lookup(ip):
	#print(ip)
	#if domain in socket.gethostbyaddr(ip)[0]:
	for domain in ips_object:
		try:
			if ipaddress.ip_address(ip) in ips_object[domain][0]:
				return domain
		except:
			pass
	return None

def button_lookup(domain):
	if domain is None:
		return None
	with open("button_mapping.json") as buttons:
		button_dict = json.load(buttons)
		for button in button_dict:
			for domains in button_dict[button]:
				if domains.lower() == domain.lower():
					return button
	return None

if __name__ == '__main__':
	pass