import os
basedir = os.path.abspath(os.path.dirname(__file__))

#path of database file
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mydb:zaqwsx999edcvfr123@mydb.cgzo8r1uo08r.us-east-1.rds.amazonaws.com:3306/3312db'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'PyTrade'
