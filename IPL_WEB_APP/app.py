from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>HELLO</h>"

app.run(debug=1,port=8000)