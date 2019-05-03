from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View
from flask_nav import Nav
import requests, json
from pprint import pprint
from wrapper import Petfinder as pc
import os

#Base of our site holds routes for API calls and js functions.
my_key = 'weKdtBuz0Oo2Qktfou38OquosnaCpilOFNqKyoay59caXNU8eI'
secret = 'ky6BRwUeDRuDcB4uPQ4G9iizplHnvfyNMBHINiZj'
type_of_pet = " "
data = {
  'grant_type': 'client_credentials',
  'client_id': my_key,
  'client_secret': secret
}
response = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)

#print(response.json())

returned = response.json()
new_data = returned['access_token']
#after token recieved
headers = {
    'Authorization': 'Bearer ' + new_data,
}

params = (
    ('type', 'cat'),
)

response = requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params)
returned = response.json()
#if(response):
	#print(returned)


topbar = Navbar('',
    View('Home', 'home'),
    View('Adoption', 'adoptions'),
)

nav = Nav()
nav.register_element('top', topbar)

app = Flask(__name__)
bootstrap = Bootstrap(app)
nav.init_app(app)

@app.route('/')
def home():
 	return render_template('home.html')

#error in here when I try to run the get_pets() method.
@app.route('/pets', methods = ['POST', 'GET'])
def pets():
  if request.method == 'POST':
    pets_type = request.form['searchbox']

  
  global returned
  #calls to the wrapper class 
  test_var = pc(my_key, secret)
  test_var.get_auth()
  test_var.print_values()
  pets_returned = test_var.get_pets(pets_type)#this causes problems other methods work.
  pprint(pets_returned)
  return render_template('products.html', test_pets=pets_returned, pets_type=pets_type)


@app.route('/adoptions')
def adoptions():  
  global returned

  return render_template('products.html', test_pets=returned)


@app.route('/details')
def details():
 	return render_template('details.html')

if __name__ == "__main__":
	app.run(debug=True)
