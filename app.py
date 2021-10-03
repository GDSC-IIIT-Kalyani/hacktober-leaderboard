from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/leaderboard") #leaderboard
def hello_world():
    return render_template("leaderboard.html")
    
@app.route("/projects")
def hello_projec():
    return render_template("projects.html")
    
    
# python code goes here
# json file savedd in ../static/data.json
    
    
if __name__ == '__main__':
    app.run(debug=True, threaded=True)