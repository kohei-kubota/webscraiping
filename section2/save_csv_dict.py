import csv

with open('top_cities.csv', 'w', newline='') as f:
  writer = csv.DictWriter(f, ['rank', 'city', 'population'])
  writer.writeheader()

  writer.writerows([
      {'rank': 1,  'city': '上海', 'population': 24150000},
      {'rank': 12, 'city': 'カラチ', 'population': 23500000},
      {'rank': 13, 'city': '北京', 'population': 21516000},
      {'rank': 14, 'city': '天津', 'population': 14722100},
      {'rank': 15, 'city': 'イスタンブル', 'population': 14160467},
    ])