# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 14:08:07 2016

@author: Shoeb
"""

from pymongo import MongoClient
import csv

client = MongoClient()
client = MongoClient('localhost',27017)

db = client.nba_database

with open(r'C:\Users\Shoeb\Documents\Python Scripts\prob.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        re = db.predictions.find({"curr":row[0],"opp":row[1]})
        if(re.count() == 0):
            result = db.predictions.insert_one(
            {
                "curr": row[0],
                "opp": row[1],
                "prob": int(row[2])
            })
            
            print result.inserted_id

            output = db.predictions.find({"curr":row[0],"opp":row[1]})
            for row in output:
                print row
            