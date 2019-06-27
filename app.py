from flask import Flask
import tensorflow
flask = Flask(__name__)

@flask.route('/')
def home():
    return "Home page"

if __name__ == '__main__':
	flask.run(use_reloader=True)