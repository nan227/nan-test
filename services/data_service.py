from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import user, book, transaction

DATABASE_URL = 'mysql://username:password@localhost/library'

def get_database_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()