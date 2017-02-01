import MySQLdb

conn = MySQLdb.connect("mydb.cgzo8r1uo08r.us-east-1.rds.amazonaws.com","mydb","zaqwsx999edcvfr123","3312db")

cur = conn.cursor()

def insert(username,email,password):
	sql = "insert into User (username,email,password) values ('%s','%s','%s')" %(username,email,password)
	cur.execute(sql)
	conn.commit()
	conn.close()

def isExisted(username,password):
	sql="select * from User where username ='%s' and password ='%s'" %(username,password)
	cur.execute(sql)
	result = cur.fetchall()
	if (len(result) == 0):
		return False
	else:
		return True

# insert("testuser","testemail","testpassword")

# print isExisted("testuser","testpassword")