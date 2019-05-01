from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View
from flask_nav import Nav


#Base of our site holds routes for API calls and js functions.


topbar = Navbar('',
    View('Home', 'home'),
    View('Adoption', 'pets'),
)

nav = Nav()
nav.register_element('top', topbar)

app = Flask(__name__)
bootstrap = Bootstrap(app)
nav.init_app(app)

@app.route('/')
def home():
 	return render_template('home.html')


@app.route('/pets')
def pets():
	test_pets = [{'name' : 'dog2', 'description' : 'blah blah blah dog2', 'image' : '"https://sunlimetech.com/portfolio/boot4menu/assets/imgs/team/img_01.png"'}, {'name' : 'dog', 'description' : 'blah blah blah dog', 'image' : '"https://sunlimetech.com/portfolio/boot4menu/assets/imgs/team/img_01.png"'}]
	return render_template('products.html', test_pets=test_pets)


@app.route('/details')
def details():
 	return render_template('details.html')

if __name__ == "__main__":
	app.run()