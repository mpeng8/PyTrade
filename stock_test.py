from app import app, db
from app.models import User, Stock

mxie33 = User.query.filter(User.username == "mxie33").first()
# fb = Stock("FB", "Facebook")
# tsx = Stock("TSX_GMO_TO", "General Electric Company")
fb = Stock.query.filter(Stock.stkid == "FB").first()
tsx = Stock.query.filter(Stock.stkid == "TSX_GMO_TO").first()
# db.session.add(fb)
# db.session.add(tsx)
# db.session.commit()
f1 = mxie33.interest_in(fb)
f2 = mxie33.interest_in(tsx)
db.session.add(f1)
db.session.add(f2)
db.session.commit()
