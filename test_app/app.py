"""
Flask API for managing books

Routes:
- POST /books: Creates a new book
- GET /books/:id: Retrieves a book by id
- PUT /books/:id: Updates a book
- DELETE /books/:id: Deletes a book
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

library = Library()

def create_new_book():
    data = {
        "id": 1,
        "title": "Book Title",
        "author": "John Doe",
        "publication_year": 2020
    }
    book = Book(**data)
    library.add_book(book)

def get_all_books():
    return library.get_books()

def update_book(id, **kwargs):
    for book in library.books:
        if book.id == id:
            book.__dict__.update(kwargs)
            return True
    return False

def delete_book(id):
    return library.delete_book(id)

@app.route('/books', methods=['POST'])
def create_new_book_api():
    new_book = request.json
    create_new_book()
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id():
    book = None
    for b in library.books:
        if b.id == id:
            book = b
            break
    return jsonify(book) if book else jsonify({"message": "Book not found"})

@app.route('/books', methods=['PUT'])
def update_book_api():
    id = request.json['id']
    updated_book = request.json
    for i, (key, value) in enumerate(updated_book.items()):
        setattr(library.books[i], key, value)
    return jsonify(updated_book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book_api():
    id = request.json['id']
    if library.delete_book(id):
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"message": "Failed to delete book"})

if __name__ == '__main__':
    app.run(debug=True)