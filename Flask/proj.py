from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View
from flask_nav import Nav
import requests, json
from pprint import pprint
from wrapper import Petfinder as pc
import config #your config file will hold your specific api key and secret if this code is to be reused.
import os

# Base of our site holds routes for API calls and js functions.

type_of_pet = " "
returned_test = {}
data = {
    'grant_type': 'client_credentials',
    'client_id': config.api_key,
    'client_secret': config.api_secret
}
response = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)


returned = response.json()
new_data = returned['access_token']
# after token recieved
headers = {
    'Authorization': 'Bearer ' + new_data,
}

params = (
     ('type', 'cat'),
 )

response = requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params)
returned = response.json()


#navbar elements
topbar = Navbar('',
                View('Home', 'home'),
                View('Adoption', 'adoptions'),
                )

nav = Nav()
nav.register_element('top', topbar)#position

app = Flask(__name__)
bootstrap = Bootstrap(app)#init a bootstrap an flask app
nav.init_app(app)#add the nave bar


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pets', methods=['POST', 'GET'])
def pets():

    '''
        function that renders a template with 
        a list of pets for adoption based of type.
    '''

    if request.method == 'POST':
        pets_type = request.form['searchbox']

    test_var = pc(config.api_key, config.api_secret)
    test_var.get_auth()
    pets_returned = test_var.get_pets(pets_type)
    returned_test = pets_returned
    
    return render_template('products.html', test_pets=pets_returned, pets_type=pets_type)


@app.route('/adoptions')
def adoptions():

    '''
        functions that renders a template for cat Adoptions.
    '''

    global returned

    return render_template('products.html', test_pets=returned['animals'])


@app.route('/details', methods=['POST'])
def details():

    '''
        this method renders a template that uses
        the selcted pet information and displays 
        more info.
    '''

    if request.method == 'POST':

        animal_id = request.form['animal_id']
        name = request.form['animal_name']
        description = request.form['animal_description']
        contact = request.form['animal_contact']
        photo = request.form['animal_photo']
        
    return render_template('details.html', photo=photo, name=name, description=description,
                           contact=contact)


if __name__ == "__main__":
    app.run(debug=True)
