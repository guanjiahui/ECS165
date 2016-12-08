import psycopg2 as dbapi
import csv
con = dbapi.connect(database="postgres", user="postgres",password="jiahui1010")
cur = con.cursor()

file = open(r'PERV2PUB.CSV', 'r')

csvObject = csv.reader(file)
list1 = list(csvObject )
head2 = list1[0]
NumVar = len(head2)

A=["%s varchar(100)"%head2[0]]
for i in range(1,NumVar):
    A.append("%s varchar(100)"%head2[i])


cur.execute("CREATE TABLE PERV2PUB (%s)"%(", ".join(A))\
            )
con.commit()


for row in list1[1:]:
    cur.execute("INSERT INTO PERV2PUB VALUES  ( %s)"%(str(row)[1:-1]))



con.commit()

cur.close()
con.close()
