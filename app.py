from flask import Flask, request, render_template
from utils.sqlServerConnector import sqlConnector

app = Flask(__name__)

@app.route('/')
def method_main():
    return render_template("index.html")


app.run(port=8000,host='localhost',debug=True)