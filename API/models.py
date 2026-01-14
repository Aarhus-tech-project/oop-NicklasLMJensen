from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50), nullable=False)
    rating = Column(Integer, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'rating': self.rating
        }
    

class Library:
    def __init__(self, session):
        self.session = session

    def add_book(self, book_instance):
            self.session.add(book_instance)
            self.session.commit()


    def get_all(self):
            all_books_as_objects = self.session.query(Book).all()
            return[b.to_dict() for b in all_books_as_objects]