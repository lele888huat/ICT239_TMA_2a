# app.py - Main Flask Application (Controller Component)

from flask import Flask, render_template
# Import the list of books from books.py
from books import all_books

app = Flask(__name__) 


# --- Helper Function ---
# Function to sort the book list by title
def sort_books(books):
    return sorted(books, key=lambda book: book['title'])


# --- Book Titles Page (Handles Initial Load and Category Filtering) ---
@app.route('/', methods=['GET'])
@app.route('/book_titles', methods=['GET'])
def book_titles():

    sorted_books = sort_books(all_books)  # Sort alphabetically by title

    return render_template(
        'book_titles.html',
        all_books=sorted_books,
    )

@app.route('/book_details/<book_title>')
def book_details(book_title):
    # For now, just a placeholder
    return f"Details for {book_title}"


if __name__ == '__main__':
    app.run(debug=True, port=5000)