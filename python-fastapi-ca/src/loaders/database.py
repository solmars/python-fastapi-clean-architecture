from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pymongo import MongoClient
import os

Base = declarative_base()

#simple singleton if used with inject
class DatabaseProvider:

    def __init__(self):
        self.sql_db_session = None
        self.mongo_db = None

    def getSQL_db_session(self):
        if self.sql_db_session is not None:
            return self.sql_db_session()
        else:
            engine = create_engine(os.getenv('SQL_DB') if os.getenv(
                'SQL_DB') is not None else ('sqlite:///:memory:'), echo=True)
            self.sql_db_session = sessionmaker(bind=engine)
            Base.metadata.create_all(engine)
            return self.sql_db_session()


    def getMongo_DB(self):
        if self.mongo_db is not None:
            return self.mongo_db
        else:
            CONNECTION_STRING = os.getenv('MONGO_DB')
            client = MongoClient(CONNECTION_STRING)
            return client.college
