
from system.core.controller import *

class Reviews(Controller):
    def __init__(self, action):
        super(Reviews, self).__init__(action)

        self.load_model('Reviewsmodel')

    def add(self):

        reviewinfo = {
        'review': request.form['review'],
        'rating': request.form['rating'],
        'user_id': session['userid'],
        'book_id': request.form['book_id']
        }
        url=reviewinfo['book_id']
        self.models['Reviewsmodel'].add(reviewinfo)
        url1="/books/"+str(reviewinfo['book_id'])

        return redirect (url1)

    def delete(self, id):
        self.models['Reviewsmodel'].delete(id)
        return redirect('/books')
