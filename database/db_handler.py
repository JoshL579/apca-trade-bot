from database.model import Base, db, Transactions
from sqlalchemy.orm import sessionmaker
from config import watching_symbol
from datetime import datetime


def init_db():
    Base.metadata.create_all(db)


def create_session():
    Session = sessionmaker(bind=db)
    return Session()


session = create_session()


def add_transaction(price):
    transaction = Transactions(
        instrument=watching_symbol,
        price=price,
        create_time=datetime.isoformat(datetime.now())
    )
    session.add(transaction)
    try:
        session.commit()
    except:
        session.rollback()
        return False
    return True


def delete_transaction(price):
    transaction = session.query(Transactions).filter_by(price=price).first()
    session.delete(transaction)
    try:
        session.commit()
    except:
        session.rollback()
        return False
    return True


def get_transactions():
    transactions = session.query(Transactions).order_by(Transactions.price).all()
    res = []
    for transaction in transactions:
        res.append(transaction)
    return res
