# Imports
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Pass a declarative base and create a object to correspond with a table in the database
Base = declarative_base()

class user(Base):

	__tablename__ = 'user'

	uid = Column(Integer, primary_key=True)
	username = Column(String(100), unique=True, nullable=False)
	pass_hash = Column(String(100), nullable=False)
	
	# Connect to and create the movie table
	engine = create_engine("sqlite:///user_database.db")
	Base.metadata.create_all(engine)
