import psycopg2

con = psycopg2.connect(host='localhost', database='dvdrental', user='postgres')

cur = con.cursor()

sql = "SELECT * FROM customer limit 10"

cur.execute(sql)

results = cur.fetchall()
for row in results:
    print(row)
    
    
cur.close()
con.close()