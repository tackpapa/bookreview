
from system.core.router import routes

routes['default_controller'] = 'Home'
routes['POST']['/users/add'] = 'Users#add'
routes['POST']['/users/login'] = 'Users#login'
routes['GET']['/books'] = 'Books#index'
routes['GET']['/books/<id>'] = 'Books#show'
routes['POST']['/reviews/add'] = 'Reviews#add'
routes['GET']['/users/<id>'] = 'Users#showuser'
routes['POST']['/books/add'] = 'Books#add'
routes['GET']['/books/addpage'] = 'Books#addpage'
routes['GET']['/users/logout'] = 'Users#logout'
routes['POST']['/delete/<id>'] = 'Reviews#delete'
