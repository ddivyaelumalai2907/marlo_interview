from Datamodel import data as D
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
DATABASE_URI = 'mysql+pymysql://sqlalchemy_user@localhost:root@localhost/marlo'

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

def get_all_data(date):
    data = session.query(D.Data).filter(date == date).all()
    return data

def fetch_speicfic_data(group):
    fetched_data = session.query(D.Data).filter_by(group_name = group).all()
    return fetched_data
