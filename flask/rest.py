from flask import Flask, jsonify, abort, request

app = Flask(__name__)


books = [
    {
        'id': 1,
        'title':'Harry Potter',
        'author': 'J.K. Rowling'
    },
    {
        'id': 2,
        'title':'Jungle Book',
        'author': 'Rudyard Kipling'
    },
    {
        'id': 3,
        'title':'Alice in Wonderland',
        'author': 'Lewis Carroll'
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book.get('id') == id:
            return jsonify({'book': book})
    abort(404)

@app.route('/books', methods=['POST'])
def create_book():
    if not request.json:
        abort(400)
    # create a new book as a dict item which can be inserted 
    # into the list
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(book)
    return jsonify({'book': book}), 201

@app.route('/books/<int:id>', methods=['PUT'])
def put_book(id):
    book = [book for book in books if book['id'] == id]

    if len(book) == 0:
        abort(404)

    if 'title' in request.json and type(request.json.get('title')) != str:
        abort(400)
    if 'author' in request.json and type(request.json.get('author')) != str:
        abort(400)

    book[0]['title'] = request.json['title']
    book[0]['author'] = request.json['author']

    return jsonify({'book': book})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)