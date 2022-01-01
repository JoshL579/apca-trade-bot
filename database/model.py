from sqlalchemy import Column, Float, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from config import database_uri


db = create_engine(database_uri)
Base = declarative_base()


class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    instrument = Column(String)
    price = Column(Float, unique=True)
    create_time = Column(String)

    def __init__(self, instrument, price, create_time):
        self.instrument = instrument
        self.price = price
        self.create_time = create_time

    def __repr__(self):
        return f"Transaction - id:{self.id}, instrument:{self.instrument}, " \
               f"price:{self.price} create_time:{self.create_time}"

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Entry(Base):
    __tablename__ = 'entry'

    id = Column(Integer, primary_key=True)
    instrument = Column(String, unique=True)
    entry = Column(Float, unique=True)
    size = Column(Float)

    def __init__(self, instrument, entry, size):
        self.instrument = instrument
        self.entry = entry
        self.size = size

    def __repr__(self):
        return f"Entry - id:{self.id}, instrument:{self.instrument}, " \
               f"entry:{self.entry} size:{self.size}"

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
