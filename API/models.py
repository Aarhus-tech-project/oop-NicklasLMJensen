from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50), nullable=False)
    chapter = Column(Integer, nullable=True)
    rating = Column(Integer, nullable=True)
    finished = Column(Integer, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'chapter': self.chapter,
            'rating': self.rating,
            'finished': self.finished
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
    
    def delete_book(self, book_id):
        book_to_delete = self.session.query(Book).get(book_id)
        if book_to_delete:
            self.session.delete(book_to_delete)
            self.session.commit()
            return True
        return False
    
    def update_book(self, book_id, data):
        book_to_update = self.session.query(Book).get(book_id)
        if book_to_update:
            for key, value in data.items():
                if hasattr(book_to_update, key):
                    setattr(book_to_update, key, value)
            self.session.commit()
            return True
        return False