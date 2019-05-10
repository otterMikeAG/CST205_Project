from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View
from flask_nav import Nav
import requests, json
from pprint import pprint
from wrapper import Petfinder as pc
import os

# Base of our site holds routes for API calls and js functions.
my_key = 'weKdtBuz0Oo2Qktfou38OquosnaCpilOFNqKyoay59caXNU8eI'
secret = 'ky6BRwUeDRuDcB4uPQ4G9iizplHnvfyNMBHINiZj'
type_of_pet = " "
data = {
    'grant_type': 'client_credentials',
    'client_id': my_key,
    'client_secret': secret
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

@app.route('/pets', methods=['POST', 'GET'])
def pets():
    if request.method == 'POST':
        pets_type = request.form['searchbox']

    test_var = pc(my_key, secret)
    test_var.get_auth()
    pets_returned = test_var.get_pets(pets_type)
    return render_template('products.html', test_pets=pets_returned, pets_type=pets_type)


@app.route('/adoptions')
def adoptions():
    global returned

    return render_template('products.html', test_pets=returned['animals'])


@app.route('/details', methods=['POST'])
def details():

    if request.method == 'POST':

        animal_id = request.form['animal_id']
        name = request.form['animal_name']
        description = request.form['animal_description']
        contact = request.form['animal_contact']
        photo = request.form['animal_photo']

    #auth = pc(my_key, secret)
    #auth.get_auth()

    #pet_photo = auth.get_photo(photo)
    #pet_name = auth.get_name(name)
    #pet_description = auth.get_description(description)
    #pet_contact = auth.get_contact(contact)

    return render_template('details.html', photo=photo, name=name, description=description,
                           contact=contact)


if __name__ == "__main__":
    app.run(debug=True)
