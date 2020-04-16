import re
from html import unescape
from urllib.parse import urljoin

with open('dp.html') as f:
  html = f.read()

for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
  url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
  url = urljoin('https://gihyo.jp/', url) # 相対URLを絶対URLに変換

  title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
  title = title.replace('<br/>', ' ')
  print(title)
  print('#####################')
  title  = re.sub(r'<.*?>', '', title) # タグを取り除く
  print(title)
  print('#####################')
  title = unescape(title) # 文字参照が含まれている場合は元に戻す(&amp;など)

  print(url, title)