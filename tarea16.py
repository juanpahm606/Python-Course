import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('Count: ', len(info['comments']))
inf=info['comments']
s=0
for item in inf:
	#print('Name:',item['name'])
	#print('Count:',item['count'])
	s=s+int(item['count'])
print('Sum: ',s)	


