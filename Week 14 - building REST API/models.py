# Przy pomocy SQLAlchemy utwórz bazę danych przechowującą produkty i opinie o produktach.
# Cechy produktu: id, nazwa, opis, kategoria
# Cechy opinii: id, autor, treść, ocena (liczbowa), produkt (którego dotyczy dana opinia)

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.orm import relationship

from main import db


class Product(db.Model):
    """
    Product model for reviewers.
    """
    __tablename__ = 'product'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(200), default='')
    description = Column(String(200), default='')
    category = Column(String(200), default='')
    reviews = relationship('Review', backref='product', lazy=True)


class Review(db.Model):
    __tablename__ = 'review'
    id = Column(Integer, autoincrement=True, primary_key=True)
    author = Column(String(200), default='')
    text = Column(String(5000), default='')
    rating = Column(Integer)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)