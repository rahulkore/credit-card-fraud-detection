from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()

########################################################################
class Account(Base):
    """"""
    __tablename__ = "acount"

    id = Column(Integer, primary_key=True)
    creditcard_number = Column(String)
    cvv = Column(String)

#----------------------------------------------------------------------
    def __init__(self, creditcard_number, cvv):
        """"""
        self.creditcard_number = creditcard_number
        self.cvv = password = cvv

# create tables
Base.metadata.create_all(engine)
