from app import db
from sqlalchemy import Sequence


class User(db.Model):
    __tablename__ = 'User'
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(30), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
    #stocks = db.Column(db.)

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
        return username
    
    @property
    def get_mail(self):
        return email
    
    @property
    def get_id(self):
        return id