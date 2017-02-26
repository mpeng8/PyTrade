from app import app, db
from app.models import User, Stock


mxie33 = User.query.filter(User.username == "mxie33").first()
yzhou = User.query.filter(User.username == "yzhou").first()
mpeng = User.query.filter(User.username == "mpeng").first()
xshi = User.query.filter(User.username == "xshi").first()


# u1 = yzhou.follow(mxie33)
# u2 = mpeng.follow(mxie33)
# u3 = xshi.follow(mxie33)

# db.session.add(u1)
# db.session.add(u2)
# db.session.add(u3)
# db.session.commit()

# print yzhou.follow(mxie33) == None
# print yzhou.is_following(mxie33)

# print yzhou.followed.count() == 1
# print yzhou.followed.first().username == 'mxie33'
# print mxie33.followers.count() == 3
# print mxie33.followers.first().username

u4 = mxie33.follow(yzhou)
db.session.add(u4)

db.session.commit()
