from api.github import Github
from flask import Flask, render_template

app = Flask(__name__)

POINTS = {"level-1" : 5, "level-2": 10, "level-3" : 20}


@app.route("/")
def home():
    return 
  
    
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
