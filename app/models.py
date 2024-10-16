from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text,ForeignKey,Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from typing import List,Set


BookAuthor = Table(
    "books_book_authors",
    Base.metadata,
    Column("book_id", ForeignKey("books_book.id"), primary_key=True),
    Column("author_id", ForeignKey("books_author.id"), primary_key=True),
    extend_existing=True,

)

BookShelf = Table(
    "books_book_bookshelves",
    Base.metadata,
    Column("book_id", ForeignKey("books_book.id"), primary_key=True),
    Column("bookshelf_id", ForeignKey("books_bookshelf.id"), primary_key=True),
    extend_existing=True,

)


BookLanguage = Table(
    "books_book_languages",
    Base.metadata,
    Column("book_id", ForeignKey("books_book.id"), primary_key=True),
    Column("language_id", ForeignKey("books_language.id"), primary_key=True),
    extend_existing=True,

)

BookSubject = Table(
    "books_book_subjects",
    Base.metadata,
    Column("book_id", ForeignKey("books_book.id"), primary_key=True),
    Column("subject_id", ForeignKey("books_subject.id"), primary_key=True),
    extend_existing=True,

)

class Subject(Base):
    __tablename__ = "books_subject"
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String, nullable=True)    
    books_book = relationship('Book', secondary=BookSubject, back_populates='books_subject')

class Language(Base):
    __tablename__ = "books_language"
    id = Column(Integer,primary_key=True,nullable=False)
    code = Column(String, nullable=True)    
    books_book = relationship('Book', secondary=BookLanguage, back_populates='books_language')


class Shelf(Base):
    __tablename__ = "books_bookshelf"
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String, nullable=True)    
    books_book = relationship('Book', secondary=BookShelf, back_populates='books_bookshelf')

class Format(Base):
    __tablename__ = "books_format"
    id = Column(Integer,primary_key=True,nullable=False)
    mime_type = Column(String, nullable=True)    
    url = Column(String, nullable=True)    
    book_id = Column(Integer,ForeignKey('books_book.id'), nullable=False)
    books_book = relationship('Book', back_populates='books_format')

class Author(Base):
    __tablename__ = "books_author"

    id = Column(Integer,primary_key=True,nullable=False)
    birth_year = Column(Integer,nullable=True)
    death_year = Column(Integer,nullable=True)
    name = Column(String, nullable=True)    
    books_book = relationship('Book', secondary=BookAuthor, back_populates='books_author')


class Book(Base):
    __tablename__ = "books_book"

    id = Column(Integer,primary_key=True,nullable=False)
    download_count = Column(Integer,nullable=True)
    gutenberg_id = Column(Integer,nullable=True)
    media_type = Column(String, nullable=True)
    title = Column(String, nullable=True)
    books_author = relationship('Author', secondary=BookAuthor, back_populates='books_book')
    books_bookshelf = relationship('Shelf', secondary=BookShelf, back_populates='books_book')
    books_language = relationship('Language', secondary=BookLanguage, back_populates='books_book')
    books_subject = relationship('Subject', secondary=BookSubject, back_populates='books_book')
    books_format = relationship('Format', back_populates='books_book')



# class BookAuthor(Base):
#     __tablename__ = "books_book_authors"

#     id = Column(Integer,primary_key=True,nullable=False)
#     # book= relationship("Book",back_populates="parent")
#     book: Mapped["Book"] = relationship()
#     book_id: Mapped[int] = mapped_column(ForeignKey("child_table.id"))


#     # book = relationship("Book", )
#     # book_id = Column(Integer,ForeignKey('books_book.id'), nullable=False)
#     # author = relationship("Author")

