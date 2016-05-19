
from system.core.model import Model

class Booksmodel(Model):
    def __init__(self):
        super(Booksmodel, self).__init__()

    def index(self):
        query = "SELECT books.title, users.id, books.id as book_id, users.name, reviews.id as review_id, reviews.rating, reviews.review, reviews.created_at from books left join reviews on reviews.book_id=books.id left join users on users.id = reviews.user_id group by books.title order by reviews.created_at DESC limit 3"
        return self.db.query_db(query)

    def titles(self):
        query ="SELECT books.id, books.title from books"
        return self.db.query_db(query)

    def showall(self, id):
        query = "SELECT books.id, books.title, books.author, reviews.review, reviews.rating, reviews.id as review_id, reviews.created_at, users.id as user_id, users.name from books left join reviews ON books.id=reviews.book_id left join users ON users.id=reviews.user_id WHERE books.id=:id order by reviews.created_at DESC"
        data = {'id': id}
        return self.db.query_db(query, data)

    def add(self, info):
        query = "INSERT INTO books (title, author, created_at, updated_at) VALUES (:title, :author, NOW(), NOW())"
        data = { 'title': info['title'], 'author': info['author'] }
        return self.db.query_db(query, data)

    def find(self, booktitle):
        query = "SELECT * from books where title=:title LIMIT 1"
        data = {'title':booktitle}
        return self.db.query_db(query, data)

    def authors(self):
        query = "SELECT books.author from books group by author"
        return self.db.query_db(query)
