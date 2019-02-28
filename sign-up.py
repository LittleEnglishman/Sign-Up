from bottle import run, route, get, post, request, view, static_file
from itertools import count
#Build Log
#V1.1 Creation of file plus test data
#V1.2 Creation of server functioanlity
#V1.5 Added in form framework
#V1.6 Added in ticket abililty/card
#V1.6.1 Added in custom css functionality
#V1.6.6 Created sell-ticket / success pages to create sell ticket system


class Ticket:
	_ids = count(0)
	
	def __init__(self,name,email,date_of_birth,check_in, image):
		self.id = next(self._ids)
		self.name = name
		self.email = email
		self.date_of_birth = date_of_birth
		self.check_in = check_in
		self.image = image

PLACEHOLDER = "image/cat.jpg"

#Ticket test data
tickets = [
    Ticket("Tommy King", "tomking@email.exmail","19/07/2001", False, PLACEHOLDER),
    Ticket("Moses Wescombe", "moseswescombe@email.email", "16/11/2007", False, PLACEHOLDER),
    Ticket("Jeremy Roberts", "jerryisdope.com", "20/02/2009", True, PLACEHOLDER),
    Ticket('Ariana Grande', "iwishihasheremail.gamil.com", "14/08/1998", False, PLACEHOLDER),
    Ticket('Dominick Rasmussen', 'email.eamil.com', '15/87/2345', False, PLACEHOLDER)
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

#check in success page
@route('/check-in-success/<ticket_id>')
@view('check-in-success')
def check_in_success(ticket_id):
	#need this function to attatch decorators above
	ticket_id = int(ticket_id)
	found_ticket = None
	for ticket in tickets:
		if ticket.id == ticket_id:
			found_ticket = ticket
			break
	data = dict (ticket = found_ticket)
	found_ticket.check_in = True
	return data
	
#sign up page with form etc Ver1.6.5
@route('/sell-ticket')
@view('sell-ticket')
def sign_up():
	pass
	
@route('/sell-ticket-success', method="POST")
@view('sell-ticket-success')
def sign_up_success():
	name = request.forms.get("name")
	email = request.forms.get("email")
	date_of_birth = request.forms.get("dob")
	
	new_ticket = Ticket(name, email, date_of_birth, False, PLACEHOLDER)
	tickets.append(new_ticket)
	
	

	

#reloader = True breaks the code? Only at home PC though???? apparantly is a server issue
run(host='localhost', port=8080, debug=True)
#run(host='0.0.0.0', port=8080, reloader= True, debug=True)
