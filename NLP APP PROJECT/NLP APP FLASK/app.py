from flask import Flask, render_template,request,redirect,session
from db import Database
from api import API
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env variables

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

dbo = Database()
apio = API()    

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register()  :
    return render_template('register.html')

@app.route('/registration', methods=["POST"])
def registration():
    name = request.form.get('username')
    email = request.form.get('email')   
    password = request.form.get('password')
    
    response = dbo.insert(name,email,password)
    
    if response:
        return render_template('login.html',message = "Registration Successfully",color ="green")
    return render_template('register.html', message = f"Email {email} already Exists!",color ="red")

@app.route('/perform_login',methods=['POST'])
def perform_login():
    email = request.form.get('email')   
    password = request.form.get('password')
    response = dbo.search(email,password)
    
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    return render_template('login.html',message = "Incorrect Email/Password" ,color = 'red')
    # return render_template('login.html', message="Incorrect Email or Password", color="red")

@app.route('/profile')
def profile():
    if session.get('logged_in'):
        return render_template('profile.html')
    return redirect('/')


@app.route('/ner')
def ner():
    if session.get('logged_in'):
        return render_template('ner.html')
    return redirect('/')

@app.route('/perform_ner',methods=['POST'])
def perform_ner():
    if not session.get('logged_in'):
        return redirect('/')

    text=request.form.get('input_text')
    response = apio.ner(text)
    return render_template('ner.html', response=response)


@app.route('/sentiment')
def sentiment():
    if session.get('logged_in'):
        return render_template('sentiment.html')
    return redirect('/')

@app.route('/perform_sentiment', methods=['POST'])
def perform_sentiment():    
    if not session.get('logged_in'):
        return redirect('/')

    text = request.form.get('input_text')
    response = apio.sentiment_analysis(text)
    return render_template('sentiment.html', response=response)
    

@app.route('/abuse_detection')
def abuse_detection():
    if session.get('logged_in'):
        return render_template('abuse_detection.html')
    return redirect('/')

@app.route('/perform_abuse_detection',methods=['POST'])
def perform_abuse_detection():
    if not session.get('logged_in'):
        return redirect('/')

    text = request.form.get('input_text')
    response = apio.abuse_detection(text)
    return render_template('abuse_detection.html', response=response)

@app.route('/summarization')
def summarization():
    if session.get('logged_in'):
        return render_template('summarization.html')
    return redirect('/')

@app.route('/perform_summarization',methods=['POST'])
def perform_summarization():
    if not session.get('logged_in'):
        return redirect('/')

    text = request.form.get('input_text')
    response = apio.summarization(text)
    return render_template('summarization.html', response=response)
    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
