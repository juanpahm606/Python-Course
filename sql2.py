import sqlite3
conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS sXs2016')
cur.execute('''CREATE TABLE IF NOT EXISTS sXs2016 (Company TEXT, 
Position TEXT, Country TEXT, Email_Hosts TEXT, Domain TEXT)''')
row=0
with open('SxSW_2016_Leads_TEST.csv', 'r') as file:
    next(file)
    for line in file:
        try:
            row = line.strip().split(',')
            cur.execute("INSERT INTO sXs2016 VALUES(?,?,?,?,?)",row)
        except:
            print("El nombre de la empresa está ente comillas")
conn.commit()            
conn.close()