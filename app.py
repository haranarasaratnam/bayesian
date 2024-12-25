'''




12/25/24 (Christmas break)
- Created skeleton to host online_course material

venv: online_course

'''


from flask import Flask, render_template
from books_data import BOOKS

app = Flask(__name__)

# Context processor to make books available globally in templates
@app.context_processor
def inject_books():
    return {'books': BOOKS}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book/<book_id>')
def book(book_id):
    book = BOOKS.get(book_id)
    return render_template('book.html', book=book, book_id=book_id)

@app.route('/book/<book_id>/chapter/<chapter_id>')
def chapter(book_id, chapter_id):
    book = BOOKS.get(book_id)
    chapter = book['chapters'].get(chapter_id) if book else None
    return render_template('book.html', book=book, chapter=chapter, book_id=book_id)

if __name__ == '__main__':
    app.run(debug=True)

