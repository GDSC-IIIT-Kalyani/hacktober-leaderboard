from flask import Flask, render_template

app = Flask(__name__)

from github import Github#entering into github
import operator
import json
dict2 = {"level-1" : 5, "level-2": 10, "level-3" : 20}
dict1={}
def func():
    g = Github("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")
    topic = 'hacktoberfest'
    ORGANIZATION = 'GDSC-IIIT-Kalyani'

    repos = g.search_repositories(query=f'topic:{topic} org:{ORGANIZATION}')
    for repo in repos:
        pull = repo.get_pulls(state='closed', sort='created', base='main')
        for pr in pull:
            dict1[pr.user.name]=[0,0,"https://github.com/"+pr.user.login+".png"]
            for label in pr.get_labels():
                if(str(label.name)=="hacktoberfest-accepted"):
                    dict1[pr.user.name][1]=1
                elif(str(label.name)== "level-1" or str(label.name)== "level-2" or str(label.name)== "level-3"):
                    dict1[pr.user.name][0]+=dict2[label.name]
    dict3 = dict( sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))
    # for key, value in dict3.items():
    #     if(value[1]==1):
    #         print(key,value[0],value[1],value[2])
    user = {}
    final_data = {}
    final_data['records'] = []
    rank = 1
    file = open("static/data2.json", "w")
    for key, value in dict3.items():
        if(value[1]==1):
            user["rank"]=rank
            user["username"]=key
            user["points"]=value[0]
            user["profileLink"]=value[2]
            #final_data.append(user)
            final_data['records'].append(user)
            user={}
            rank+=1
    data = json.dumps(final_data, indent=4)
    file.write(data)
    file.close
func()

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