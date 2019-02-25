from bottle import run, route, get, post, request, view, static_file
from itertools import count
#Build Log
#V1.1 Creation of file plus test data
#V1.2 Creation of server functioanlity
#V1.5 Added in form framework
#V1.6 Added in ticket abililty/card
#V1.6.1 Added in custom css functionality

class Ticket:
	_ids = count(0)
	
	def __init__(self,name,email,date_of_birth,check_in):
		self.id = next(self._ids)
		self.name = name
		self.email = email
		self.date_of_birth = date_of_birth
		self.check_in = check_in
		
#Ticket test data
tickets = [
    Ticket("Tommy King", "tomking@email.exmail","19/07/2001", True),
    Ticket("Moses Wescombe", "moseswescombe@email.email", "16/11/2007", False),
    Ticket("Jeremy Roberts", "jerryisdope.com", "20/02/2009", True),
    Ticket('Ariana Grande', "iwishihasheremail.gamil.com", "14/08/1998", False),
    Ticket('Dominick Rasmussen', 'email.eamil.com', '15/87/2345', False)
    ]


#Images
@route('/image/<filename>')
def server_static(filename):
	return static_file(filename, root='./assets/images')

	
#Pages
#1.2 Server functionality
#index page
@route('/')
@view('index')

def index():
	#need this function to attatch decorators above
	pass


#Code to be able to link custom css (this works) Ver1.6.1
@route('/<filename>.css')
def stylesheets(filename):
    return static_file('{}.css'.format(filename), root='./assets')



#check-in page route V1.6
@route('/check-in')
@view('check-in')

def check_in():
	data = dict (ticket_list = tickets)
	return data

#reloader = True breaks the code? Only at home PC though???? apparantly is a server issue
run(host='localhost', port=8080, debug=True)
#run(host='0.0.0.0', port=8080, reloader= True, debug=True)
