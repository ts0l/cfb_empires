# %%
import requests
import json
import csv

URL= 'https://api.collegefootballdata.com/'
param = {"year":"2018" , "week":"1"}
responses = requests.get(URL+'games', param).json()

x= len(responses)
i = 0
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
 
param1 = {"year":"2018" , "week":"2"}
param2 = {"year":"2018" , "week":"3"}
param3 = {"year":"2018" , "week":"4"}
param4 = {"year":"2018" , "week":"5"}
param5 = {"year":"2018" , "week":"6"}
param6 = {"year":"2018" , "week":"7"}
param7 = {"year":"2018" , "week":"8"}
param8 = {"year":"2018" , "week":"9"}
param9 = {"year":"2018" , "week":"10"}
param10 = {"year":"2018" , "week":"11"}
param11 = {"year":"2018" , "week":"12"}
param12 = {"year":"2018" , "week":"13"}
param13 = {"year":"2018" , "week":"14"}





def get_values(aList):
  responses = aList
  for i in range(x):
    one_game = responses[i]
    team1_score.append(one_game["home_points"])
    team2_score.append(one_game["away_points"])
    team1_name.append(one_game["home_team"])
    team2_name.append(one_game["away_team"])
    i= i+1 
    
def determine_winner():
  winning_team = []
  for i in range(x):
    score_diff = team1_score[i] - team2_score[i]
    if score_diff > 0:
      winning_team.append(team1_name[i])
    else:
      winning_team.append(team2_name[i])
  i = i+1
  print(winning_team)
  
get_values(responses)
determine_winner()
w_teams_1 = winning_team


responses_1 = requests.get(URL+'games', param1).json()
i = 0
x = len(responses_1)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_1)
determine_winner()
w_teams_2 = winning_team


responses_2 = requests.get(URL+'games', param2).json()
i = 0
x = len(responses_2)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_2)
determine_winner()
w_teams_3 = winning_team

responses_3 = requests.get(URL+'games', param3).json()
i = 0
x = len(responses_3)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_3)
determine_winner()
w_teams_4 = winning_team

responses_4 = requests.get(URL+'games', param4).json()
i = 0
x = len(responses_4)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_4)
determine_winner()
w_teams_5 = winning_team

responses_5 = requests.get(URL+'games', param5).json()
i = 0
x = len(responses_5)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_5)
determine_winner()
w_teams_6 = winning_team

responses_6 = requests.get(URL+'games', param6).json()
i = 0
x = len(responses_6)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_6)
determine_winner()
w_teams_7 = winning_team

responses_7 = requests.get(URL+'games', param7).json()
i = 0
x = len(responses_7)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_7)
determine_winner()
w_teams_8 = winning_team

responses_8 = requests.get(URL+'games', param8).json()
i = 0
x = len(responses_8)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_8)
determine_winner()
w_teams_9 = winning_team

responses_9 = requests.get(URL+'games', param9).json()
i = 0
x = len(responses_9)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_9)
determine_winner()
w_teams_10 = winning_team

responses_10 = requests.get(URL+'games', param10).json()
i = 0
x = len(responses_10)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_10)
determine_winner()
w_teams_11 = winning_team


responses_11 = requests.get(URL+'games', param11).json()
i = 0
x = len(responses_11)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_11)
determine_winner()
w_teams_12 = winning_team

responses_12 = requests.get(URL+'games', param12).json()
i = 0
x = len(responses_12)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_12)
determine_winner()
w_teams_13 = winning_team

responses_13 = requests.get(URL+'games', param13).json()
i = 0
x = len(responses_13)
team1_score = []
team2_score = []
team1_name = []
team2_name = []
winning_team = []
get_values(responses_13)
determine_winner()
w_teams_14 = winning_team


from itertools import zip_longest
d = [w_teams_1, w_teams_2, w_teams_3, w_teams_4, w_teams_5, w_teams_6, w_teams_7, w_teams_8, w_teams_9, w_teams_10, w_teams_11, w_teams_12, w_teams_13, w_teams_14]
export_data = zip_longest(*d, fillvalue = '')
with open('w_teams.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Week1", "Week2", "Week3", "Week4", "Week5", "Week6", "Week7", "Week8", "Week9", "Week10", "Week11", "Week12", "Week13", "Week14"))
      wr.writerows(export_data)
myfile.close()

# %%
