from database.model import Base, db, Transactions, Entry
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


def get_entry():
    entry = session.query(Entry).first()
    return entry.entry


def get_lot_size():
    entry = session.query(Entry).first()
    return entry.size


def add_entry(size):
    entry = Entry(
        instrument=watching_symbol,
        entry=0,
        size=size
    )
    session.add(entry)
    try:
        session.commit()
    except:
        session.rollback()
        return False
    return True
