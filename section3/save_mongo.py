import lxml.html
from pymongo import MongoClient

client  = MongoClient('localhost', 27017)
# データベースが存在しない場合でも書き込み時に自動的に作成される
db = client.scraping # scrapingデータベースを取得
collection = db.books

# コレクションのドキュメントを全て削除する
collection.delete_many({})

# HTMLファイル読み込み
tree = lxml.html.parse('dp.html')
html = tree.getroot()

# hrefのリンクを絶対パスに変更する
html.make_links_absolute('https://gihyo.jp/')

# a要素を取得
for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
  url  = a.get('href')
  # print(a.cssselect('p[itemprop="name"]'))
  p = a.cssselect('p[itemprop="name"]')[0]

  title = p.text_content()

  collection.insert_one({'url': url, 'title': title})

for link in collection.find().sort('_id'):
  print(link['_id'], link['url'], link['title'])

