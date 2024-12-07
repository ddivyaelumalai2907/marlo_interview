from sqlalchemy import create_engine, Column, Integer, String, Date,BigInteger
from sqlalchemy.orm import declarative_base

# Database Configuration
DATABASE_URI = 'mysql+pymysql://sqlalchemy_user@localhost:root@localhost/marlo'

# Initialize Engine
engine = create_engine(DATABASE_URI)

# Base for ORM Models
Base = declarative_base()


class Data(Base):
    __tablename__ = 'data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    group_name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    value = Column(BigInteger, nullable=False)

