
from flask import Blueprint, jsonify, abort, make_response

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Natascha",
        "message": "You got this, guuuurl!", 
        "hobbies": ["Reading", "Playing Video Games","Hiking", "Traveling"]
    }

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Natascha",
        "message": "You got this, guuuurl!", 
        "hobbies": ["Reading", "Playing Video Games","Hiking", "Traveling"]
    }
    new_hobby = ["Eating"]
    response_body["hobbies"] = response_body["hobbies"] + new_hobby
    return response_body

class Book: 
    def __init__(self, id, title, description): 
        self.id = id
        self.title = title
        self.description = description
    
books = [
    Book(1, "Pride and Prejudice", "A fantasy novel set in an imaginary world."),
    Book(2, "Harry Potter", "A fantasy novel set in an imaginary world."),
    Book(3, "Mexican Gothic", "A fantasy novel set in an imaginary world.")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id, 
            "title": book.title, 
            "description": book.description
        })
    return jsonify(books_response)

def validate_book(book_id): 
    try:
        book_id = int(book_id)
    except: 
        abort(make_response({"message":f"book {book_id} invalid"}, 400))
    
    for book in books:
        if book.id == book_id:
            return book
    
    abort(make_response({"message":f"book {book_id} not found"}, 404))

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book = validate_book(book_id)
    
    return {
        "id": book.id, 
        "title": book.title,
        "description": book.description
    }
