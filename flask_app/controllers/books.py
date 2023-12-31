from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import book, author # can import class due to no risk of circular imports, correct? more helpful to import file rather than class into models.

# @app.route('/')
# def books():
#     return redirect("/books")

# ! SHOW ALL BOOKS (READ)
# ! FORM VIEW
@app.route('/books')
def show_all_books():
    all_books=book.Book.get_all_books()
    # print(all_books[0], "*"*20)
    return render_template('books.html',book_list = all_books)

# ! INVISIBLE (CREATE)
@app.route('/book/create', methods=['POST'])
def add_book():
    book.Book.add_new_book(request.form)
    return redirect('/books')

# ! SHOW ONE BOOK (READ)
# ! SHOW ALL AUTHORS WHO HAVE FAVORED IT (READ)
# ! FORM VIEW (dropdown of all authors who haven't yet favored?)
@app.route('/book/<int:id>')
def show_one_book_with_faving_authors(id):
    this_books_authors = book.Book.get_one_book_with_favoring_authors(id)
    all_authors = author.Author.get_all_authors()
    # not_yet_faving_authors = book.Book.get_one_books_not_yet_faving_authors(id)
    return render_template('one_book.html', this_book = this_books_authors, all_authors = all_authors)
    # return render_template('one_book.html', this_book = this_books_authors, not_yet_faving_authors = not_yet_faving_authors)




# # ! INVISIBLE (CREATE)
# @app.route('/add/book/<int:id>/to/authors_favs', methods=['POST']) # do I need to use the ID variable in this route?
# def this_book_added_to_an_authors_favs(author_id): # Would this be the exact same method as this_author_pics_a_favorite in authors.py? And when do I call the thing being passed in author_ID or ID in this case isn't it better to distinguish one foreign key from the other?

    # data = {
    #         "author_id": author_id
    #     }
    
    # data = {
    #         "author_id": int(data['author_id']),
    #         "book_id":int(data['book_id'])
    #     }
    # faving_author = author.Author.add_a_favorite(id)
    # return redirect(f'/book/{request.form["id"]}', faving_author = faving_author)