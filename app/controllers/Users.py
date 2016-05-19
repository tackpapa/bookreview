
from system.core.controller import *
from time import strftime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from flask.ext.bcrypt import Bcrypt

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('Usersmodel')
        # self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def add(self):

        error=False

        if len(request.form['name']) < 2:
            flash('name should be longer than 2 letters')
            error=True

        if len(request.form['alias']) < 2:
            flash('name should be longer than 2 letters')
            error=True

        if not EMAIL_REGEX.match(request.form['email']):
            flash("email not valid!", 'regis')
            error=True


        if len(request.form['pw']) < 2:
            flash("password should be longer than 2 letters!")
            error=True

        pw = request.form['pw']
        cpw = request.form['cpw']
        if cpw != pw:
            flash("pw doesn't match you idiot!")
            error=True
        if error == True:
            return redirect('/')

        info={
        'name':request.form['name'],
        'alias':request.form['alias'],
        'email':request.form['email'],
        'pw': request.form['pw']
        }
        self.models['Usersmodel'].add(info)
        return redirect ('/')

    def login(self):
        email=request.form['email']
        pw=request.form['pw']
        info={
        'email':email,
        'pw': pw
        }

        user=self.models['Usersmodel'].login(info)
        print user
        if user==False:
            flash('invalid email or password')
            return redirect('/')
        elif user:
            session['userid'] = user[0]['id']
            session['name'] = user[0]['name']
            session['email']=user[0]['email']
            session['alias']=user[0]['alias']
            session['status']=True
            return redirect('/books')

    def logout(self):
        session['email']=[]
        session['alias']=[]
        session['name']=[]
        session['userid']=[]
        session['status']=False
        return redirect ('/')


    def showuser(self, id):
        users=self.models['Usersmodel'].showuser(id)
        books=self.models['Usersmodel'].showbooks(id)
        return self.load_view('users.html', users=users, books=books)
