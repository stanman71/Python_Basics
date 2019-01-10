from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine('mysql+pymysql://python:python@localhost/python'))
session = scoped_session(Session)

