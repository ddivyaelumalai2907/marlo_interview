from sqlalchemy import create_engine, Column, Integer, String, SmallInteger
from sqlalchemy.orm import declarative_base

# Database Configuration
DATABASE_URI = 'mysql+pymysql://sqlalchemy_user@localhost:root@localhost/marlo'

# Initialize Engine
engine = create_engine(DATABASE_URI)

# Base for ORM Models
Base = declarative_base()

# Define Model
class MarloUser(Base):
    __tablename__ = 'marlo_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email_id = Column(String(255), nullable=False)
    role_id = Column(SmallInteger, nullable=False)
Base.metadata.create_all(engine)