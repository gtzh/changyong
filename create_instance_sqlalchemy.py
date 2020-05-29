#!/usr/bin/env python
# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

uri = "mysql+pymysql://bttzh:bttzh664956@tttzh.f3322.net:13306/bthome?charset=utf8mb4&binary_prefix=true"
Base = declarative_base()
engine = create_engine(uri)
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
    

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', nickname='windy'),
#     User(name='mary', fullname='Mary Contrary', nickname='mary'),
#     User(name='fred', fullname='Fred Flintstone', nickname='freddy')
# ])
# session.commit()
