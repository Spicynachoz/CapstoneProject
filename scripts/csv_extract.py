# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 13:50:03 2016

@author: htanwar
"""

import csv
import os

'''
    This script is used to extract data from a csv
    file which contains data from previous seasons
    of nba games.
    
    You enter the team you're looking for, which will later 
    be put through an Artificial Neural Network
    in another script
    
    Format is the following:
    [Home, score, Away, score, wins_home, losses_home, 
    wins_away, losses_away, w/l % home, w/l % away, 
    point_difference, (win or loss o your team)]

'''

if __name__ == "__main__":
    file = open('nba_data.csv')
    csv_read = csv.reader(file)
    team = input ("Enter team name: ")
    home_wins = 0
    away_wins = 0
    losses_away = 0
    losses_home = 0
    for row in csv_read:
        if(row[0] == team or row[2] == team):
            if (row[0] == team):
                if(int(row[1]) > int(row[3])):
                    home_wins += 1
                    win = 1
                else:
                    losses_home += 1
                    win = 0
                score_diff = int(row[1]) - int (row[3]) 
            if (row[2] == team):
                if(int(row[1]) < int(row[3])):
                   away_wins += 1
                   win = 1
                else:
                    losses_away += 1
                    win = 0
            row[4] = home_wins
            row[5] = losses_home
            row[6] = away_wins
            row[7] = losses_away
            if ( home_wins + losses_home > 0):
                row[8] = ((home_wins) / (home_wins + losses_home))
            if( away_wins + losses_away > 0):
                row[9] = ((away_wins) / (away_wins + losses_away))
            if(int(row[1]) > int(row[3])):
                point_diff = int(row[1]) - int(row[3])
            else:
                point_diff = int(row[3]) - int(row[1])
            row[10] = point_diff
            row.append(win)
            print (row)
            
