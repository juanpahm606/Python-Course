from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count=input('Enter count: ')
position=input('Enter position: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
links=list()
# Retrieve all of the anchor tags
tags = soup('a')
i=0
c=int(count)
p=int(position)
print('Retrieving:',url)
while i<=c-1:
    i=i+1
    url=tags[p-1].get('href', None)
    print('Retrieving:', url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')