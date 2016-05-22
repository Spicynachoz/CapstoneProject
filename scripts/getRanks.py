# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:26:10 2016

@author: htanw
"""

import csv

def setRanks():
    file = open('nba_data.csv')
    file2 = open('ranks.csv')
    read = csv.reader(file)
    read2 = csv.reader(file2)
    rank_list = []
    for ranks in read2:
        rank_list.append(ranks)
    with open('test.csv', 'w', newline='') as fp:
        temp = csv.writer(fp)
        for row in read:
            for rank in rank_list:
                if(rank[1] == row[0]):
                    row[0] = (30 - int(rank[0])) + 1
                if(rank[1] == row[2]):
                    row[2] = (30 - int(rank[0])) + 1
            temp.writerow(row)
            

def arrange():
    file = open('test.csv')
    file2 = open('ranks2.csv')
    read1 = csv.reader(file)
    read2 = csv.reader(file2)
    rank_list = []
    read = []
    for ranks in read2:
        rank_list.append(ranks)
        print (ranks)
    for t in read1:
        read.append(t)
    with open('nba_ranks_data.csv', 'w', newline = '') as fp:
        temp = csv.writer(fp)
        for team in rank_list:
            info = []
            home_wins = 0
            away_wins = 0
            losses_away = 0
            losses_home = 0
            winLossStreak = 0
            for row in read:
                if(row[0] == team[1] or row[2] == team[1]):
                    if (row[0] == team[1]):
                        if(int(row[1]) > int(row[3])):
                            if (winLossStreak < 0):
                                winLossStreak = 1
                            else:
                                winLossStreak +=1 
                                home_wins += 1
                                win = 1
                        else:
                            losses_home += 1
                            win = 0
                            if (winLossStreak > 0):
                                winLossStreak = -1
                            else:
                                winLossStreak -= 1
                    if (row[2] == team[1]):
                        if(int(row[1]) < int(row[3])):
                            away_wins += 1
                            win = 1
                            if (winLossStreak < 0):
                                winLossStreak = 1
                            else:
                                winLossStreak +=1 
                        else:
                            losses_away += 1
                            win = 0
                            if (winLossStreak > 0):
                                winLossStreak = -1
                            else:
                                winLossStreak -= 1                    
                    row[4] = home_wins
                    row[5] = losses_home
                    row[6] = away_wins
                    row[7] = losses_away
                    if ( home_wins + losses_home > 0):
                        row[8] = ((home_wins) / (home_wins + losses_home))
                    if( away_wins + losses_away > 0):
                        row[9] = ((away_wins) / (away_wins + losses_away))
                    row[10] = winLossStreak
                    row[11] = win
                    temp.writerow(row)
             
    

if __name__ == '__main__':
    arrange()
                    