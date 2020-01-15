import mysql.connector
c=mysql.connector.connect(host='localhost',user='root',passwd='',database='demo1')
cur=c.cursor()
cur.execute("delete from student where rollno=4")
c.commit()
c.close()