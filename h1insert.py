import psycopg2 as dbapi
import csv
con = dbapi.connect(database="postgres", user="postgres",password="jiahui1010")
cur = con.cursor()

file = open(r'EIA_CO2_Electricity_2015.CSV', 'r')

csvObject = csv.reader(file)
list1 = list(csvObject )
head = list1[0]
NumVar = len(head)

A=["%s varchar(100)"%head[0]]
for i in range(1,NumVar):
    A.append("%s varchar(100)"%head[i])


cur.execute("CREATE TABLE EIA_CO2_Electricity(%s)"%(", ".join(A))\
            )
con.commit()


for row in list1[1:]:
    cur.execute("INSERT INTO EIA_CO2_Electricity VALUES  ( %s)"%(str(row)[1:-1]))



con.commit()

cur.close()
con.close()
