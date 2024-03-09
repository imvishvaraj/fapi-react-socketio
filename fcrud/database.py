from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://mfinuser:135mfin456@localhost:5432/expensesdb")
meta = MetaData()
conn = engine.connect()
Base = declarative_base()
session_local = sessionmaker(bind=engine)