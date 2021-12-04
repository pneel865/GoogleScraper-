from flask import Flask 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c6275dd74b8478932e00973af22d2919'

from flasksite import routes
