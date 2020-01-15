import pymysql
c=pymysql.connect(host='localhost',user='root',passwd='',database='demo1')
cur=c.cursor()
cur.execute("insert into student values(4,'jasprit','bumrah',3500)")
c.commit()
c.close()