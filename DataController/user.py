from Datamodel import users
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
DATABASE_URI = 'mysql+pymysql://sqlalchemy_user@localhost:root@localhost/marlo'

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

def get_all_users():
    return session.query(users.MarloUser).all()

def create_user(name, email_id, role_id):
    new_user = users.MarloUser(name=name, email_id=email_id, role_id=role_id)
    session.add(new_user)
    session.commit()
    return new_user
def login_auth(email):
    user = session.query(users.MarloUser).filter_by(email_id=email).first()
    if user is not None:
        return user
    return None