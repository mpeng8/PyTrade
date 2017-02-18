from app import app, db
from app.models import User, Stock


u1 = User(username='mjxie', email='m1xie@example.com', password="111111")
u2 = User(username='jjthomson', email='j1thomson@example.com', password="111111")
db.session.add(u1)
db.session.add(u2)
db.session.commit()
#create relation of follow
print u1.unfollow(u2) == None
u = u1.follow(u2)
# create follower
db.session.add(u)
db.session.commit()
print u1.follow(u2) == None
print u1.is_following(u2)
print u1.followed.count() == 1
print u1.followed.first().username == 'jjthomson'
print u2.followers.count() == 1
print u2.followers.first().username == 'mjxie'
u = u1.unfollow(u2)
print u != None
db.session.add(u)
db.session.commit()
print not u1.is_following(u2)
print u1.followed.count() == 0
print u2.followers.count() == 0
User.query.filter(User.id == u1.id).delete()
User.query.filter(User.id == u2.id).delete()
db.session.commit()
