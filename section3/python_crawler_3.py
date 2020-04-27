from typing import Iterator
import time
import re
import requests
import lxml.html
from pymongo import MongoClient

def main():
  client = MongoClient('localhost', 27017)
  collection = client.scraping.ebooks
  collection.create_index('key', unique=True)

  session = requests.Session()

  response = requests.get('https://gihyo.jp/dp')
  urls = scrape_list_page(response)
  for url in urls:
    key = extract_key(url)

    ebook = collection.find_one({'key': key})
    if not ebook:
      time.sleep(1) # サーバー負荷を下げる
      response = session.get(url)
      ebook = scrape_detail_page(response)
      print(ebook)
      # break # テスト用に１ページで抜ける

def scrape_list_page(response: requests.Response) -> Iterator[str]:
  html = lxml.html.fromstring(response.text)
  html.make_links_absolute(response.url)

  for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
    url = a.get('href')
    yield url

def scrape_detail_page(response: requests.Response) -> dict:
  """
  詳細ページから情報をdictで取得する
  """
  html = lxml.html.fromstring(response.text)
  ebook = {
    'url': response.url,
    'title': html.cssselect('#bookTitle')[0].text_content(),
    # 'price': html.cssselect('.buy')[0].text, # 末尾に余計な空白が入る
    'price': html.cssselect('.buy')[0].text.strip(),
    # 'content':[h3.text_content() for h3 in html.cssselect('#content > h3')], # 余計な空白が入る
    'content':[normalize_spaces(h3.text_content()) for h3 in html.cssselect('#content > h3')],
  }

  return ebook

def extract_key(url: str) -> str:
  m = re.search(r'/([^/]+)$', url) # 最後の/から末尾までの文字列を取得
  return m.group(1)


def normalize_spaces(s: str) -> str:
  return re.sub(r'\s+','', s).strip()


if __name__ == '__main__':
  main()

