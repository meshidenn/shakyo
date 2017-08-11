import sys
import urllib
from urllib.request import urlopen

url = 'https://gihyo.jp/dp'
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"}
req = urllib.request.Request(url, None, headers)
f = urlopen(req)
encoding = f.info().get_content_charset(failobj="utf-8")
print('encoding:', encoding, file=sys.stderr)

text = f.read().decode(encoding)
print(text)
