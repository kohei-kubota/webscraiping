import csv

with open('top_cities.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(['rank', 'city', 'population'])
  writer.writerows([
    [1,  '上海', 24150000],
    [12, 'カラチ', 23500000],
    [13, '北京', 21516000],
    [14, '天津', 14722100],
    [15, 'イスタンブル', 14160467],
  ])