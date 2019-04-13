import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createuser import *

engine = create_engine('sqlite:///tutorial.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin","password")
session.add(user)

user = User("rahul","password")
session.add(user)

user = User("rohit","password")
session.add(user)

# commit the record the database
session.commit()

session.commit()
