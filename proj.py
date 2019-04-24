from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View
from flask_nav import Nav


# To keep things clean, we keep our Flask-Nav instance in here. We will define
# frontend-specific navbars in the respective frontend, but it is also possible
# to put share navigational items in here.


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
 	return render_template('products.html')

@app.route('/details')
def details():
 	return render_template('details.html')

if __name__ == "__main__":
	app.run()