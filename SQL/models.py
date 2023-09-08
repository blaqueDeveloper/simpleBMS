from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')
    comments = relationship('Comment', back_populates='book')

class Reader(Base):
    __tablename__ = 'readers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    comments = relationship('Comment', back_populates='reader')

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    book_id = Column(Integer, ForeignKey('books.id'))
    reader_id = Column(Integer, ForeignKey('readers.id'))
    reader_name = Column(String)

    book = relationship('Book', back_populates='comments')
    reader = relationship('Reader', back_populates='comments')