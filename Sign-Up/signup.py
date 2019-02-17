from bottle import run, route, get, push
#Build Log
#V1.1 Creation of file plus test data
#V1.2 Creation of server functioanlity

#Ticket test data
tickets = [
    Ticket("Thomas John King", "tomking@email.exmail","19/07/2001"),
    Ticket("Moses Wescombe", "moseswescombe@email.email", "16/11/2007"),
    Ticket("Jeremy Roberts", "jerryisdope.com", "20/02/2009"),
    Ticket('Ariana Grande', "iwishihasheremail.gamil.com", "14/08/1998")
    ]
	
#Pages
#1.2 Server functionality
#index page
@route('/')
@view('/index.')

def index():
	#need this function to attatch decorators above
	pass
	
run(host='0.0.0.0', port=8080, reloader= True, debug=True)
