import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createaccount import *

engine = create_engine('sqlite:///tutorial.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

account = Account("123456789","123")
session.add(account)

account = Account("987654321","123")
session.add(account)

account = Account("9552139510","123")
session.add(account)

# commit the record the database
session.commit()

session.commit()
