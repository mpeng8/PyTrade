from app import db
from sqlalchemy import Sequence

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('User.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('User.id'))
)

stock_list_table = db.Table('fav_stock_list',
    db.Column('user_id', db.Integer, db.ForeignKey('User.id')),
    db.Column('stk_id', db.String(64), db.ForeignKey('Stock.stkid'))
)

class User(db.Model):
    __tablename__ = 'User'
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(30), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
    stocks = db.relationship('Stock',
                                secondary= stock_list_table,
                                primaryjoin=(stock_list_table.c.user_id == id), 
                                backref=db.backref('fav_stock', lazy='dynamic'),
                                lazy='dynamic')

    # reference microblog
    followed = db.relationship('User',
                               secondary=followers, 
                               primaryjoin=(followers.c.follower_id == id), 
                               secondaryjoin=(followers.c.followed_id == id), 
                               backref=db.backref('followers', lazy='dynamic'), 
                               lazy='dynamic')

    # constraints not finished
    # __table_args__ = (
    #             CheckConstraint(len(password) >= 6, name="check_password_len"),
    #             CheckConstraint(
    #                     username ~* '^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$',
    #                     name="user_valid_username",
    #             ),
    #             {})

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User(name='%s', id='%s')>" % (self.username, self.id)

    @property
    def get_name(self):
        return self.username

    @property
    def get_mail(self):
        return self.email

    @property
    def get_id(self):
        return str(self.id).encode("utf-8").decode("utf-8") 

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False


    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def insterest_in(self, stock):
        if not stock_in_list(stock):
            self.stocks.append(stock)
            return self

    def delete_stk(self, stock):
        if stock_in_list(stock):
            stocks.remove(stock)

    def stock_in_list(self, stock):
        return self.stocks.filter(stocks.c.stkid == stock.stkid).count() > 0

class Stock(db.Model):
    __tablename__ = 'Stock'
    stkid = db.Column(db.String(64), index=True, primary_key=True, nullable=False)

    def __init__(self, stkid):
        self.stkid = stkid


    def __repr__(self):
        return "<Stock(stkid='%s')>" % (self.stkid)
