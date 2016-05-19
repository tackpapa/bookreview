
from system.core.controller import *

class Home(Controller):
    def __init__(self, action):
        super(Home, self).__init__(action)


    def index(self):
        if session['name']:
            return redirect ('/books')

        return self.load_view('index.html')
