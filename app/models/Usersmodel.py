
from system.core.model import Model
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from flask.ext.bcrypt import Bcrypt

class Usersmodel(Model):
    def __init__(self):
        super(Usersmodel, self).__init__()


    def add(self, info):
        pw = info['pw']
        hashed_pw = self.bcrypt.generate_password_hash(pw)
        query = "INSERT into users (name, alias, email, created_at, updated_at, pw) values(:name, :alias, :email, NOW(), NOW(), :pw)"
        data = {'name': info['name'], 'alias': info['alias'], 'email': info['email'],'pw':hashed_pw}
        return self.db.query_db(query, data)


    def login(self, info):
        pw = info['pw']
        email = info['email']
        userquery = "SELECT * FROM users WHERE email = :email LIMIT 1"
        userdata = {'email': email}

        user = self.db.query_db(userquery, userdata)
        if user:
            if self.bcrypt.check_password_hash(user[0]['pw'], pw):
               return user
        return False

    def showuser(self, id):
        query = "select users.alias, users.name, users.email, count(reviews.id) as total from users left join reviews on users.id=reviews.user_id left join books on reviews.book_id=books.id where users.id=:id"
        data = {'id': id}
        return self.db.query_db(query, data)

    def showbooks(self, id):
        query = "select users.id, books.id as book_id, books.title from users left join reviews on users.id=reviews.user_id left join books on reviews.book_id = books.id where users.id=:id"
        data = {'id':id}
        return self.db.query_db(query, data)
