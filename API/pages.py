from flask import Blueprint, render_template, request, Flask, jsonify
from models import db, Book, Library



bp = Blueprint("pages", __name__)




@bp.route("/")
def home():
    
    return render_template("pages/home.html")



@bp.route("/books", methods=["POST"])
def add_book():
    my_library = Library(db.session)

    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    book = Book(
        title=data.get('Bname'),
        author=data.get('Aname'),
        chapter=data.get('chapter'),
        rating=data.get('Rating'),
        finished=1 if data.get('finished') else 0
    )
    my_library.add_book(book)
    from flask import redirect, url_for
    return redirect(url_for('pages.home'))


@bp.route("/books", methods=["GET"])
def get_books():
    my_library = Library(db.session)
    all_books = my_library.get_all()
    return jsonify(all_books), 200


@bp.route("/books/<int:id>", methods=["DELETE"])
def remove_book(id):
    my_library = Library(db.session)
    success = my_library.delete_book(id)

    if success:
        return {"message": "Book deleted successfully"}, 200
    return {"message": "Book not found"}, 404

@bp.route("/books/<int:id>", methods=["PATCH"])
def update_book(id):
    data = request.get_json(silent=True)
    my_library = Library(db.session)

    success = my_library.update_book(id, data)

    if success:
        return {"message": "Book updated successfully"}, 200
    return {"message": "Book not found"}, 404

@bp.route("/list")
def list_books():
    my_library = Library(db.session)
    all_books = my_library.get_all()
    return render_template("pages/List.html", books=all_books)