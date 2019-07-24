from flask import Flask, render_template


app = Flask(__name__)
app.debug = True 

@app.route('/')

@app.route('/home')
def home():
    return render_template('homePage.html')

@app.route('/interviews')
def interview():
    return render_template('interviews.html')

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about')
def about():
    return render_template('about.html')

