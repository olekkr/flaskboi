from flask import Flask, url_for, render_template
from markupsafe import escape 


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    print(url_for('profile', username=username))
    return '{}\'s profile'.format(escape(username))

@app.route('/fart')
def test():
    print(10)
    return render_template('template.html', name = "")

@app.route('/xss=<input>')
def xss(input):
    print(input)
    return render_template('template.html', name = input)
 
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))