# pip install sqlalchemy-repr
#!/usr/bin/env python

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):

    """ Database informations """

    __tablename__ = 'user'
    
    id       = Column(Integer, primary_key=True)
    username = Column(String(15), unique=True)
    email    = Column(String(50), unique=True)
    password = Column(String(80))


if __name__ == "__main__":
    
    from sqlalchemy import create_engine
    from settings import DB_URI
    
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
