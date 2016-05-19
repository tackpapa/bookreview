
from system.core.controller import *

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        self.load_model('Booksmodel')
        self.load_model('Reviewsmodel')
        # self.db = self._app.db

    def index(self):
        books=self.models['Booksmodel'].index()
        titles=self.models['Booksmodel'].titles()
        return self.load_view('books.html', books=books, titles=titles)

    def show(self, id):
        books=self.models['Booksmodel'].showall(id)
        session['book_id']=books[0]['id']
        return self.load_view('show.html', books=books)

    def addpage(self):
        books=self.models['Booksmodel'].authors()
        return self.load_view('add.html', books=books)

    def add(self):
        if request.form['author']:
            author = request.form['author']
        if request.form['authorpick']=="none":
            author = request.form['author']
        if request.form['authorpick'] !="none":
            author = request.form['authorpick']


        booktitle = request.form['title']

        info={
            'title':request.form['title'],
            'author':author
        }
        self.models['Booksmodel'].add(info)
        books=self.models['Booksmodel'].find(booktitle)
        print books
        reviewinfo={
            'review': request.form['review'],
            'rating': request.form['rating'],
            'user_id': session['userid'],
            'book_id': books[0]['id']
        }
        url1="/books/"+str(reviewinfo['book_id'])
        self.models['Reviewsmodel'].add(reviewinfo)

        return redirect (url1)
