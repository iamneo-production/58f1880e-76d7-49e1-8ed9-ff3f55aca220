import os 
from flask import Flask
app=Flask(__name__)
@app.route("/")
def main():
    return "welcome"
@app.route('/how are you')
def hello():
   return 'I am good,how are you'
if __name__=="__main__":
    app.run()
    