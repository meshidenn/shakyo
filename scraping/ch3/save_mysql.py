# -*- coding: utf-8 -*-

import psycopg2

conn = psycopg2.connect(host='localhost',dbname='scraping', user='scraper', password='password')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS cites')
c.execute('''
    CREATE TABLE cites(
        rank integer,
        city text,
        population integer
    )
''')

c.execute('INSERT INTO cites VALUES(%s, %s, %s)', (1, '上海', 24150000))

c.execute('INSERT INTO cites VALUES (%(rank)s, %(city)s, %(population)s)',
          {'rank':2, 'city':'カラチ', 'population':23500000})

c.executemany('INSERT INTO cites VALUES (%(rank)s, %(city)s, %(population)s)',[
          {'rank':3, 'city':'北京', 'population':21516000},
          {'rank':4, 'city':'イスタンブル', 'population':14160467}])

conn.commit()

c.execute('SELECT * FROM cites')

for row in c.fetchall():
    print(row)

conn.close()
