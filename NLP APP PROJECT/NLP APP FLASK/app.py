from flask import Flask, render_template,request,redirect
from db import Database
from api import API

app = Flask(__name__)

dbo = Database()
apio = API()

@app.route('/')
def index():
    # return "Hello worl/s !"
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
        return redirect('/profile')
    return render_template('login.html',message = "Incorrect Email/Password" ,color = 'red')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner',methods=['POST'])
def perform_ner():
    text=request.form.get('input_text')
    response = apio.ner(text)
    print(response)
    
    return render_template('ner.html', response=response)










@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')

@app.route('/perform_sentiment', methods=['POST'])
def perform_sentiment():
    text = request.form.get('input_text')
    response = apio.sentiment_analysis(text)
    return render_template('sentiment.html', response=response)
    

@app.route('/abuse_detection')
def abuse_detection():
    return render_template('abuse_detection.html')

@app.route('/perform_abuse_detection',methods=['POST'])
def perform_abuse_detection():
    text = request.form.get('input_text')
    response = apio.abuse_detection(text)
    return render_template('abuse_detection.html', response=response)

@app.route('/summarization')
def summarization():
    return render_template('summarization.html')

@app.route('/perform_summarization',methods=['POST'])
def perform_summarization():
    text = request.form.get('input_text')
    response = apio.summarization(text)
    return render_template('summarization.html', response=response)
    

if __name__ == '__main__':
    app.run(debug=True)
