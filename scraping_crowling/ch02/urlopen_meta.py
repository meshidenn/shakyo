import re
import sys
import urllib
from urllib.request import urlopen

url = 'https://gihyo.jp/dp'
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"}
req = urllib.request.Request(url, None, headers)
f = urlopen(req)
bytes_content = f.read()

acanned_text = bytes_content[:1024].decode('ascii', errors='replace')
match = re.search('charset=["\'\?([\w-]+)', scanned_text)
if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8'

print('encoding:', encoding, file=sys.stderr)
text = bytes_content.decode(encoding)
print(text)
