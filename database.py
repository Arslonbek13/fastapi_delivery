from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



engine = create_engine('postgresql://postgres:Arslonbek0413@localhost/fast_delivery_db', echo=True)


Base = declarative_base()
session = sessionmaker()

