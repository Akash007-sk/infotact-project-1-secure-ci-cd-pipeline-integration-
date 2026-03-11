from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def home():
    return "DevSecOps Security Test App"

@app.route('/login')
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    query = "SELECT * FROM users WHERE username='"+username+"' AND password='"+password+"'"

    return "Query executed: " + query

app.run(host="0.0.0.0",port=5000)
