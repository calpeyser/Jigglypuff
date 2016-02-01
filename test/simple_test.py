import requests
import json

params = json.dumps({'chorale': open('parallel_unison.xml', 'rb').read()})
r = requests.post('http://192.168.99.101:8080/check', params)

print r.json()