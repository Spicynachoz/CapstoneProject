# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 17:21:09 2016

@author: Shoeb
"""

from bs4 import BeautifulSoup as bs
import urllib2
import re
import json
import pymongo
from pymongo import MongoClient


def getLink(team1,team2):
    url = 'http://espn.go.com/nba/team/stats/_/name/' + team1 + '/year/2015/split/'
    response = urllib2.urlopen(url)
    html = response.read()
    soup = bs(html,'html.parser')
    
    for link in soup.find_all('a'):
        if(link.get('href')):          
            if(re.findall('nba/team/stats/_/name/' + team1 + '/year/2015/split/([0-2]?[0-9]||30)/', link.get('href')) != []):            
                teamName = (link.string)
                teamName = teamName.lower()
                teamName = teamName.replace(' ', '-')
                if(teamDict[team2] == teamName):
                    return link.get('href')

url = 'http://espn.go.com/nba/teams'
response = urllib2.urlopen(url)
html = response.read()

soup = bs(html,'html.parser')

teamDict = dict()

for link in soup.find_all('a'):
    if(link.get('href')):
        if(re.findall('team\/_\/name', link.get('href')) != []):
            team = link.get('href').split('/')
            teamID = team[7]
            teamName = team[8]
            teamDict[teamID] = teamName
            
response = urllib2.urlopen(url)
html = response.read()
soup = bs(html,'html.parser')

#team1 = raw_input('Enter first team: ').lower()
#team2 = raw_input('Enter second team: ').lower()
team1 = 'gsw'
team2 = 'bos'

url =  getLink(team1,team2)
response = urllib2.urlopen(url)
html = response.read()
soup = bs(html,'html.parser')

playerList = list()

for link in soup.find_all('tr',class_=lambda x:x == 'oddrow' or x == 'evenrow'):
   player = list()
   for child in link.children:
      for ch in child:
          try:
              if(re.findall(',',ch) != []):
                  pass
              else:
                  player.append(ch)
          except TypeError:
              if(len(ch.string) != 1):
                  player.append(ch.string)
   playerList.append(player)

stat = dict()
playerDict = dict()
for player in playerList:
    stat=dict()
    if(not playerDict.has_key(player[0])):
        playerDict[player[0]] = dict()
        playerDict[player[0]]['name'] = player[0]
        playerDict[player[0]][team2] = dict()
        playerDict[player[0]][team2]['stats'] = dict()
        playerDict[player[0]][team2]['stats']['GP'] = player[1]
        playerDict[player[0]][team2]['stats']['GS'] = player[2]
        playerDict[player[0]][team2]['stats']['MIN'] = player[3]
        playerDict[player[0]][team2]['stats']['PPG'] = player[4]
        playerDict[player[0]][team2]['stats']['OFFR'] = player[5]
        playerDict[player[0]][team2]['stats']['DEFR'] = player[6]
        playerDict[player[0]][team2]['stats']['RPG'] = player[7]
        playerDict[player[0]][team2]['stats']['APG'] = player[8]
        playerDict[player[0]][team2]['stats']['SPG'] = player[9]
        playerDict[player[0]][team2]['stats']['BPG'] = player[10]
        playerDict[player[0]][team2]['stats']['TPG'] = player[11]
        playerDict[player[0]][team2]['stats']['FPG'] = player[12]
        
    elif(playerDict.has_key(player[0])):
        playerDict[player[0]][team2]['stats']['FGM'] = player[1]
        playerDict[player[0]][team2]['stats']['FGA'] = player[2]
        playerDict[player[0]][team2]['stats']['FGP'] = player[3]
        playerDict[player[0]][team2]['stats']['3PM'] = player[4]
        playerDict[player[0]][team2]['stats']['3PA'] = player[5]
        playerDict[player[0]][team2]['stats']['3PP'] = player[6]
        playerDict[player[0]][team2]['stats']['FTM'] = player[7]
        playerDict[player[0]][team2]['stats']['FTA'] = player[8]
        playerDict[player[0]][team2]['stats']['FTP'] = player[9]
        playerDict[player[0]][team2]['stats']['2PM'] = player[10]
        playerDict[player[0]][team2]['stats']['2PA'] = player[11]
        playerDict[player[0]][team2]['stats']['2PP'] = player[12]
        playerDict[player[0]][team2]['stats']['AFG'] = player[13]


with open('playerData.json', 'w') as d:
    for player in playerDict.keys():
        json.dump(playerDict[player], d, indent=4,sort_keys=True)
        
'''with pen('playerData.json', 'w') as d:
    json.dump(playerDict, d,indent=4,sort_keys=True)
'''

stats = list()
for link in soup.find_all('tr',class_=lambda x:x == 'total'):
    totals = list()
    for child in link.children:
      for ch in child:
          try:
              if(re.findall('Totals',ch) != [] or re.findall('--',ch) != []):
                  pass
              else:
                  totals.append(ch)
          except TypeError:
              #totals.append(ch.string)
              pass
    stats.append(totals)

teamDict[team1] = dict()
teamDict[team1]['name'] = team1
teamDict[team1]['opp'] = dict()

teamDict[team1]['opp'][team2] = dict()
teamDict[team1]['opp'][team2]['stats'] = dict()
teamDict[team1]['opp'][team2]['stats']['GP'] = stats[0][0]
teamDict[team1]['opp'][team2]['stats']['PPG'] = stats[0][1]
teamDict[team1]['opp'][team2]['stats']['OFFR'] = stats[0][2]
teamDict[team1]['opp'][team2]['stats']['DEFR'] = stats[0][3]
teamDict[team1]['opp'][team2]['stats']['RPG'] = stats[0][4]
teamDict[team1]['opp'][team2]['stats']['APG'] = stats[0][5]
teamDict[team1]['opp'][team2]['stats']['SPG'] = stats[0][6]
teamDict[team1]['opp'][team2]['stats']['BPG'] = stats[0][7]
teamDict[team1]['opp'][team2]['stats']['TPG'] = stats[0][8]
teamDict[team1]['opp'][team2]['stats']['FPG'] = stats[0][9]

teamDict[team1]['opp'][team2]['stats']['FGM'] = stats[1][0]
teamDict[team1]['opp'][team2]['stats']['FGA'] = stats[1][1]
teamDict[team1]['opp'][team2]['stats']['FGP'] = stats[1][2]
teamDict[team1]['opp'][team2]['stats']['3PM'] = stats[1][3]
teamDict[team1]['opp'][team2]['stats']['3PA'] = stats[1][4]
teamDict[team1]['opp'][team2]['stats']['3PP'] = stats[1][5]
teamDict[team1]['opp'][team2]['stats']['FTM'] = stats[1][6]
teamDict[team1]['opp'][team2]['stats']['FTA'] = stats[1][7]
teamDict[team1]['opp'][team2]['stats']['FTP'] = stats[1][8]
teamDict[team1]['opp'][team2]['stats']['2PM'] = stats[1][9]
teamDict[team1]['opp'][team2]['stats']['2PA'] = stats[1][10]
teamDict[team1]['opp'][team2]['stats']['2PP'] = stats[1][11]

with open('teamData.json', 'w') as d:
    json.dump(teamDict[team1], d,indent=4,sort_keys=True)
    
client = MongoClient()
db = client.scores
#db.scores.delete_many({})
for player in playerDict.keys():
    result = db.scores.insert_one(playerDict[player])
print result
db.scores.insert_one(teamDict[team1])
