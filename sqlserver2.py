import pymysql
c=pymysql.connect(host='localhost',user='root',passwd='',database='demo1')
cur=c.cursor()
cur.execute("update student set fees=fees+1000 where rollno=1")
cur.execute("update student set fees=fees+500 where rollno=2")
c.commit()
c.close()