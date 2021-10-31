import os, json, operator
from github import Github  # entering into github
from flask import Flask, render_template, send_from_directory

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

json_url = os.path.join(SITE_ROOT, 'static', 'data2.json')
data = json.load(open(json_url))
# print(data)
app = Flask(__name__)

dict2 = {"level-1" : 5, "level-2": 10, "level-3" : 20, "Level-1" : 5, "Level-2": 10, "Level-3" : 20}
dict1={}
def func():
    g = Github("github_token")
   
    org = g.get_organization("GDSC-IIIT-Kalyani")
    org.login
    #adding the required repos under Hacktoberfest
    repos=[]
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/Winter-of-Code-2.0-frontend"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/ENCODN"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/winter-of-code"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/WOC-certificate-generator-Hactoberfest2021"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/placement-portal"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/Pandemic-Simulator"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/FUSION_VAE_DSC"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/todo-tracker"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/Eagle-AI-GUI"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/Space-Invaders"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/Paint"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/playground"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/PaperVault"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/hacktober-leaderboard"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/Tic-Tac-Toe"))
    repos.append(g.get_repo("GDSC-IIIT-Kalyani/flutter-url-launcher"))

    for repo in repos:
        print(repo.name)
        print("\n")
        pull = repo.get_pulls('closed')

        for pr in pull:
            if pr.user.name in dict1.keys():
                for label in pr.get_labels():
                    if(str(label.name)=="hacktoberfest-accepted"):
                        dict1[pr.user.name][1]=1
                    elif(str(label.name)== "level-1" or str(label.name)== "level-2" or str(label.name)== "level-3" or str(label.name)== "Level-1" or str(label.name)== "Level-2" or str(label.name)== "Level-3"):
                        dict1[pr.user.name][0]+=dict2[label.name]
            else:        
                dict1[pr.user.name]=[0,0,"https://github.com/"+pr.user.login+".png"]
                for label in pr.get_labels():
                    if(str(label.name)=="hacktoberfest-accepted"):
                        dict1[pr.user.name][1]=1
                    elif(str(label.name)== "level-1" or str(label.name)== "level-2" or str(label.name)== "level-3" or str(label.name)== "Level-1" or str(label.name)== "Level-2" or str(label.name)== "Level-3"):
                        dict1[pr.user.name][0]+=dict2[label.name]
    dict3 = dict( sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))
    for key, value in dict3.items():
        if((value[1]==1) and (value[0]!=0)):
            print(key,value[0],value[1],value[2])
    user = {}
    final_data = {}
    final_data['records'] = []
    rank = 1
    file = open("static/data2.json", "w")
    for key, value in dict3.items():
        if((value[1]==1) and (value[0]!=0)):
            user["rank"]=rank
            user["username"]=key
            user["points"]=value[0]
            user["profileLink"]=value[2]
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
    return render_template("leaderboard.html", data = data)
    
@app.route("/projects")
def hello_projec():
    return render_template("projects.html")
    



  
    
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
