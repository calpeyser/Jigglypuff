import requests
import json

params = json.dumps({'chorale': open('parallel_unison.xml', 'rb').read()})
r = requests.post('http://localhost:8000/check', params)

print r.json()