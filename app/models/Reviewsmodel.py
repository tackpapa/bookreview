
from system.core.model import Model

class Reviewsmodel(Model):
    def __init__(self):
        super(Reviewsmodel, self).__init__()

    def showall(self, id):
        query = "Select * from reviews where book_id=:id"
        data = {'book_id': id}
        return self.db.query_db(query, data)

    def add(self, reviewinfo):
        query = "INSERT INTO reviews (review, rating, created_at, updated_at, user_id, book_id) VALUES (:review, :rating, NOW(), NOW(), :user_id, :book_id)"
        data = {
        'review': reviewinfo['review'],
        'rating': reviewinfo['rating'],
        'user_id': reviewinfo['user_id'],
        'book_id': reviewinfo['book_id']
        }
        return self.db.query_db(query, data)

    def delete(self, id):
        query="DELETE from reviews where id=:id"
        data = {'id': id}
        return self.db.query_db(query, data)
