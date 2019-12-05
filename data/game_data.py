# %%
import requests
import json

URL= 'https://api.collegefootballdata.com/'
 
param = {"year":"2018" , "week":"1"}
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


responses = requests.get(URL+'games', param).json()

x= len(responses)
i = 0
team1_score = []
team2_score = []
team1_name = []
team2_name = []

def get_values():
  for i in range(x):
    one_game = responses[i]
    team1_score.append(one_game["home_points"])
    team2_score.append(one_game["away_points"])
    team1_name.append(one_game["home_team"])
    team2_name.append(one_game["away_team"])
    i= i+1 
    


get_values()
print("Current Values found for the 1st week and for all programs")
print(team1_score)
print(team2_score)
print(team1_name)
print(team2_name)


# %%
