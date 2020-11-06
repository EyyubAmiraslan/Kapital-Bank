from flask import Flask, render_template, request
import  os

app = Flask(__name__, static_url_path = "", static_folder = "static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:example@127.0.0.1:3306/BankKapital'

app.config['SECRET_KEY'] = os.urandom(16)

from models import *
from controllers import *





if __name__ == '__main__':
    app.run(debug=True)