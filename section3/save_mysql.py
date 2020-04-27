import MySQLdb

conn = MySQLdb.connect(db='scraping', user='scraper', passwd='password', charset='utf8mb4')

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS `cities`')
c.execute("""
  CREATE TABLE `cities` (
    `rank` integer,
    `city` text,
    `populaton` integer
  )
""")

c.execute('INSERT INTO `cities` VALUES (%s, %s, %s)', (1, '上海', 2415000))

# パラメータが辞書の場合、プレースホルダーは%(名前)sで指定する
c.execute('INSERT INTO `cities` VALUES (%(rank)s, %(city)s, %(population)s)',
          {'rank':2, 'city': 'カラチ', 'population': 23500000})


# executemany()は複数のパラメータをリストで指定して、複数のSQL文を実行する
c.executemany('INSERT INTO `cities` VALUES (%(rank)s, %(city)s, %(population)s)',[
  {'rank': 3, 'city': '北京', 'population': 21516000},
  {'rank': 4, 'city': '天津', 'population': 14722100},
  {'rank': 5, 'city': 'イスタンブル', 'population': 14160467},
])

conn.commit()

c.execute('SELECT * FROM `cities`')
for row in c.fetchall():
  print(row)

conn.close()
