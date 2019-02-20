from bottle import run, route, get, post, request, view, static_file
from itertools import count
#Build Log
#V1.1 Creation of file plus test data
#V1.2 Creation of server functioanlity

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
    Ticket("Thomas John King", "tomking@email.exmail","19/07/2001", True),
    Ticket("Moses Wescombe", "moseswescombe@email.email", "16/11/2007", False),
    Ticket("Jeremy Roberts", "jerryisdope.com", "20/02/2009", True),
    Ticket('Ariana Grande', "iwishihasheremail.gamil.com", "14/08/1998", False)
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

#reloader = True breaks the code? Only at home PC though???? apparantly is a server issue
#run(host='localhost', port=8080, debug=True)
run(host='0.0.0.0', port=8080, reloader= True, debug=True)
