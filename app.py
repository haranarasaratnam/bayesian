'''




12/25/24 (Christmas break)
- Created skeleton to host online_course material

venv: online_course

'''

from flask import Flask, render_template, abort, jsonify
from books_data import BOOKS

app = Flask(__name__)

# Context processor for global access to books
@app.context_processor
def inject_books():
    return {'books': BOOKS}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book/<book_id>')
def book(book_id):
    book = BOOKS.get(book_id)
    if not book:
        abort(404)
    return render_template('book.html', book=book, book_id=book_id)

# API route to dynamically load chapter/subchapter content
@app.route('/book/<book_id>/chapter/<chapter_id>/load')
def load_chapter(book_id, chapter_id):
    book = BOOKS.get(book_id)
    if not book:
        abort(404)
    chapter = book['chapters'].get(chapter_id)
    if not chapter:
        abort(404)
    #return render_template(chapter['template'])

@app.route('/book/<book_id>/chapter/<chapter_id>/subchapter/<subchapter_id>/load')
def load_subchapter(book_id, chapter_id, subchapter_id):
    book = BOOKS.get(book_id)
    if not book:
        abort(404)
    chapter = book['chapters'].get(chapter_id)
    if not chapter:
        abort(404)
    subchapter = chapter['subchapters'].get(subchapter_id)
    if not subchapter:
        abort(404)
    return render_template(subchapter['template'])

if __name__ == '__main__':
    app.run(debug=True)
