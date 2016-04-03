import requests
import json
import sys

REMOTE_IP = "104.196.109.169"
LOCAL_IP = "192.168.99.100"

def run_test(ip_address):
	params = json.dumps({'chorale': open('parallel_unison.xml', 'rb').read()})
	r = requests.post('http://%s:8080/check' % ip_address, params)

	print r.json()

if __name__ == "__main__":
	if len(sys.argv) < 2:
		run_test(LOCAL_IP)
	elif sys.argv[1] != "remote":
		run_test(LOCAL_IP)
	else:
		run_test(REMOTE_IP)