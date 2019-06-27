#!/usr/bin/python

import jwt

payload = {'foo': 'bar'}

with open('key.txt', 'r') as key_file:
	global key
	key = key_file.read()

print key

encoded = jwt.encode(payload, key, algorithm='HS256')
print encoded

decoded = jwt.decode(encoded, key, algorithms=['HS256'])
print decoded
