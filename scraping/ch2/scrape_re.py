import re
from html import unescape

with open('dp') as f:
    html = f.read()

    print(type(html))

a = re.findall(r'<a itemprop="url".*?</ul>.*</a></li>',html, re.DOTALL)
#print(a)
    
for i,partial_html in enumerate(re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>',html, re.DOTALL)):
#    print(i,partial_html)
    url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
    url = 'https"//gihyo.jp' + url

    title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
    title = title.replace('<br/>','')
    title = re.sub(r'<.*?>','',title)

    print(url,title)


