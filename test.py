#!/usr/bin/env python
# coding=utf-8
for row in session.query(User, User.name).all():
    print(row.User, row.name)

building a Relationship

from sqlalchemy import ForeignKey
from sqlal:q

