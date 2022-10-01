import os, json                   # for file handling
from github import Github         # for accessing github data
from datetime import datetime     # for datetime object
from operator import itemgetter   # for sorting nested list
from flask import Flask, render_template, send_from_directory


# Setting and loading the main export data file:
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'static', 'data2.json')
data = json.load(open(json_url))

# if os.path.exists('data2.json'):
#     json_url = 'data2.json'
#     data = json.load(open(json_url))

# Initializing the flask app:
app = Flask(__name__)

# Info to edit for 2022:
label_for_hacktober_2022 = "hacktoberfest"
label_accepted_pull = "hacktoberfest-accepted"
event_starting_date = datetime(2021, 10, 1)

levels = {"level-1" : 5, "level-2": 10, "level-3" : 20, "Level-1" : 5, "Level-2": 10, "Level-3" : 20}

# Hard-Coded data (All GDSC_IIIT_KALYANI's repo):
all_repos = ['GDSC-IIIT-Kalyani/CogniWapp', 'GDSC-IIIT-Kalyani/Eagle-AI-GUI', 'GDSC-IIIT-Kalyani/ENCODN', 'GDSC-IIIT-Kalyani/flutter-url-launcher', 'GDSC-IIIT-Kalyani/FUSION_VAE_DSC', 'GDSC-IIIT-Kalyani/hacktober-leaderboard', 'GDSC-IIIT-Kalyani/Image-Classification-by-Federated-Learning', 'GDSC-IIIT-Kalyani/javascript', 'GDSC-IIIT-Kalyani/MediCare-Prime', 'GDSC-IIIT-Kalyani/Paint', 'GDSC-IIIT-Kalyani/Pandemic-Simulator', 'GDSC-IIIT-Kalyani/PaperVault', 'GDSC-IIIT-Kalyani/placement-portal', 'GDSC-IIIT-Kalyani/playground', 'GDSC-IIIT-Kalyani/qwiklabs_challenges', 'GDSC-IIIT-Kalyani/RAKSHA', 'GDSC-IIIT-Kalyani/Space-Invaders', 'GDSC-IIIT-Kalyani/start-git', 'GDSC-IIIT-Kalyani/Student-Portfolio', 'GDSC-IIIT-Kalyani/Tic-Tac-Toe', 'GDSC-IIIT-Kalyani/todo-tracker', 'GDSC-IIIT-Kalyani/winter-of-code', 'GDSC-IIIT-Kalyani/winter-of-code-2.0-backend', 'GDSC-IIIT-Kalyani/Winter-of-Code-2.0-frontend', 'GDSC-IIIT-Kalyani/Winter-of-Code-IIIT-Kalyani-1.0', 'GDSC-IIIT-Kalyani/WOC-certificate-generator-Hactoberfest2021'] # information fetched by Sagar's wrapper API


# Main loop function:
def func():
    # Accessing main github page of GDSC-IIIT-KALYANI:
    g = Github("github_token")
    org = g.get_organization("GDSC-IIIT-Kalyani")
    org.login

    # Filtering the repos made available for hacktoberfest-2022 one-time operation:
    if os.path.exists('static/hack_repos.txt'):
        with open('static/hack_repos.txt', 'r') as f:
            hack_repos = eval(f.read())
    else:
        hack_repos = []   # This list will contain all the hackable 2022 repos name
        for repo in all_repos:
            rep = g.get_repo(repo)
            labels = rep.get_labels()

            if label_for_hacktober_2022 in [label.name for label in labels]:
                hack_repos.append(rep.full_name)

        with open('static/hack_repos.txt', 'w') as f:   # writing (hack_repos) to the external file for re-usability
            f.write(str(hack_repos))

    # LeaderBoard Logic:
    ranks = []
    done_users = []
    for rep in hack_repos:
        repo = g.get_repo(rep)
        pulls = repo.get_pulls(state='closed')   # getting all the closed pull requests
        
        for pr in pulls:
            pr_labels = [label.name for label in pr.get_labels()]
            # Accepted pull reqs that are of current month:
            if (pr.created_at > event_starting_date) and (label_accepted_pull in pr_labels):
                score = 0
                for k, v in levels.items():   # calculating score from the level dictionary
                    if k in pr_labels:
                        score = v
                
                if pr.user.name in done_users:
                    for i in range(len(ranks)):
                        if ranks[i][0] == pr.user.name:
                            ranks[i][1] += (-score)
                            break
                else:
                    # Making a nested list (ranks):
                    # ranks = [['uname', '-score', 'img_url', 'first_pull_req_date&time'], ...] (-score would be taken care of later)
                    ranks.append([pr.user.name, -score, "https://github.com/"+pr.user.login+".png", pr.created_at])
                    done_users.append(pr.user.name)
   
    # Sorting rank according to the score then the date & time of first pull req. per user:
    ranks = sorted(ranks, key=itemgetter(1, 2), reverse=True)
    ranks = ranks[::-1]
    # print(ranks)

    # Populating the final export data with rank detail based on the ranks list:
    rank = 1
    user = {}
    data = {}
    data['records'] = []
    with open("static/data2.json", "w") as f:
        for i in ranks:
            user["rank"] = rank
            user["username"] = i[0]
            user["points"] = -i[1]
            user["profilelink"] = i[2]
            data['records'].append(user)
            user = {}
            rank+=1
        data = json.dumps(data, indent=4)
        f.write(data)

func()


# URL routings:
@app.route("/")
def start():
    return render_template("index.html")

@app.route("/leaderboard") #leaderboard
def hello_world():
    return render_template("leaderboard.html", data = data)
    
@app.route("/projects")
def hello_projec():
    return render_template("projects.html")
  

# Main:
if __name__ == '__main__':
    app.run(debug=True, threaded=True)