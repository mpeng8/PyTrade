from coverage import coverage
cov = coverage(branch=True, omit=['flask/*', 'db_test.py'])
cov.start()

import os
import unittest
from datetime import datetime, timedelta

from app import app, db
from app.models import User, Stock


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mydb:zaqwsx999edcvfr123@mydb.cgzo8r1uo08r.us-east-1.rds.amazonaws.com:3306/3312db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_follow_unfollow(self):
    	# create 2 user
        u1 = User(username='mjxie', email='mjxie@example.com', password="111111")
        u2 = User(username='jjthomson', email='jjthomson@example.com', password="111111")
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        # create relation of follow
        assert u1.unfollow(u2) is None
        u = u1.follow(u2)
        # create follower
        db.session.add(u)
        db.session.commit()
        assert u1.follow(u2) is None
        assert u1.is_following(u2)
        assert u1.followed.count() == 1
        assert u1.followed.first().username == 'jjthomson'
        assert u2.followers.count() == 1
        assert u2.followers.first().username == 'mjxie'
        u = u1.unfollow(u2)
        assert u is not None
        db.session.add(u)
        db.session.commit()
        assert not u1.is_following(u2)
        assert u1.followed.count() == 0
        assert u2.followers.count() == 0

    def test_add_stocks(self):
        # make 1 user
        u1 = User(nickname='sjb', email='sjb@example.com')
        db.session.add(u1)
        # make 2 stocks
        s1 = Stock(stkid = 'fb')
        s2 = Stock(stkid = 'nvda')
        db.session.add(s1)
        db.session.add(s2)
        db.session.commit()
        u1.insterest_in(s1)
        assert u1.stocks.



    def test_delete_post(self):
        # create a user and a post
        u = User(nickname='john', email='john@example.com')
        p = Post(body='test post', author=u, timestamp=datetime.utcnow())
        db.session.add(u)
        db.session.add(p)
        db.session.commit()
        # query the post and destroy the session
        p = Post.query.get(1)
        db.session.remove()
        # delete the post using a new session
        db.session = db.create_scoped_session()
        db.session.delete(p)
        db.session.commit()

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print "\n\nCoverage Report:\n"
    cov.report()
    cov.html_report(directory='tmp/coverage')
    cov.erase()