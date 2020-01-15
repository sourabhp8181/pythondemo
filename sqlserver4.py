import pymysql
c=pymysql.connect(host='localhost',user='root',passwd='',database='demo1')
cur=c.cursor()
x=cur.execute("select * from student")
p=cur.fetchall()
for i in p:
	print ("%d\t%s\t%s\t%d"%(i[0],i[1],i[2],i[3]))
c.close()