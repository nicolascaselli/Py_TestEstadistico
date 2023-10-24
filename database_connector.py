import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect_to_mysql(database_url):
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    return engine, Session()
