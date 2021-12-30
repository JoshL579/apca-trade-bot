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
    create_time = Column(DateTime)

    def __init__(self, instrument, price, create_time):
        self.instrument = instrument
        self.price = price
        self.create_time = create_time

    def __repr__(self):
        return f"User - id:{self.id}, instrument:{self.instrument}, " \
               f"price:{self.price} create_time:{self.create_time}"

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
