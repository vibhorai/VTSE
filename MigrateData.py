

import json
import sqlite3 as db
import pandas as pd

df = pd.read_json('E://MTP//Misc//supersite.json')
con = db.connect('db.sqlite3')
cursor = con.cursor()
cursor.execute('''create table VedicText (title TEXT, translation TEXT, url TEXT)''')


for index, row in df.iterrows():
    for element in row.items():
        try:
            title = element[1]['title']
        except:
            title = ''
        try:
            translation = json.dumps(element[1]['translation'])
        except:
            translation = ''
        try:
            url = element[1]['url']
        except:
            url = ''
        

        cursor.execute("INSERT INTO VedicText VALUES (?,?,?)", ('title','translation','url'))

con.commit()
con.close()        