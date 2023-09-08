from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


# Database setup
engine = create_engine('sqlite:///my_database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Creating the tables
Base.metadata.create_all(engine)
