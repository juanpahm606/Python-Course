import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url=input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
names = tree.findall('.//name')
s=0
print('Count:', len(counts))
#print('Names count :', len(names))
#for name in names:
#    print('Name:',name.text)
for count in counts:
#    print('Count',count.text)
    s=s+int(count.text)
print('Sum:',s)      
