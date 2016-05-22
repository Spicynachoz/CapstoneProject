# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:36:29 2016

@author: htanwar
"""

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import FullConnection
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.utilities import percentError

import csv

from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.customxml import NetworkWriter
from pybrain.tools.customxml import NetworkReader

import data_extract

def neuralNet(info, test_data):
    ann = FeedForwardNetwork()
    
    ''' 
        Initiate the input nodes, hidden layer nodes,
        and the output layer nodes.
    '''
    inputLayer = LinearLayer(5)
    hiddenLayer = SigmoidLayer(20) 
    outputLayer = LinearLayer(1)
    
    '''
        Add the nodes to the corresponding layer
    '''
    ann.addInputModule(inputLayer)
    ann.addModule(hiddenLayer)
    ann.addOutputModule(outputLayer)
    
    '''
        Connect the input layer to hidden layer,
        then connect hidden layer to output layer
    '''
    in_to_hidden = FullConnection(inputLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outputLayer)
    
    ann.addConnection(in_to_hidden)
    ann.addConnection(hidden_to_out)
    
    ann.sortModules ()
    
    data_set = SupervisedDataSet(5, 1)
    for data in info:
        data_set.addSample(data[:-1], data[-1])
    trainer = BackpropTrainer(ann, data_set, verbose=False)
    
    #test_data, train_data = data_set.splitWithProportion(0.2)
    train_data = data_set
    test_data = test_data
    '''
        Using 50 epochs for testing purposes, it will train
        the network until convergence within the first 50 epochs
    
    '''
    train = trainer.trainUntilConvergence(dataset=train_data, maxEpochs=10)
    NetworkWriter.writeToFile(ann, 'filename5.xml')
    
    for d in test_data:
        out = ann.activate(d)
        #print (train)
        print (out) 
        
    '''
    trainError = percentError (trainer.testOnClassData(), train_data) 
    testError = percentError (trainer.testOnClassData(dataset = test_data), test_data)
    print ("  train error: %5.3f%%" % trainError)
    print ("  test error: %5.3f%%" % testError)
    '''
    
def test(filename, test_data):
    ann = NetworkReader.readFrom(filename)
    #file = open('results.csv', 'w', newline = ' ')
    rank_teams = {1: 'Philadelphia 76ers', 2: 'Los Angeles Lakers', 3: 'Brooklyn Nets', 4: 'Phoenix Suns', 
             5: 'Minnesota Timberwolves', 6: 'New Orleans Pelicans', 7: 'New York Knicks', 
             8: 'Sacramento Kings', 9: 'Milwaukee Bucks', 10: 'Denver Nuggets', 11: 'Orlando Magic', 
             12: 'Utah Jazz', 13: 'Washington Wizards', 14: 'Houston Rockets', 15: 'Chicago Bulls', 
             16: 'Memphis Grizzlies', 17: 'Dallas Mavericks', 18: 'Portland Trail Blazers', 
             19: 'Detroit Pistons', 20: 'Indiana Pacers', 21: 'Miami Heat',
             22: 'Charlotte Hornets', 23: 'Boston Celtics', 24: 'Atlanta Hawks', 
             25: 'Los Angeles Clippers', 26: 'Oklahoma City Thunder', 27: 'Toronto Raptors', 
             28: 'Cleveland Cavaliers', 29: 'San Antonio Spurs', 30: 'Golden State Warriors'}
    list_ = []
    with open('temp_file2.csv', 'w', newline = '') as fp:
        temp = csv.writer(fp)
        for i in range(1,31):
            for j in range(1, 31):
                if(i != j):
                    out = ann.activate([i, j, 0, 0, 0])
                    if (out > 1.00):
                        out = 99
                    else:
                        num = out * 100
                        out = int(num)
                    temp.writerow([rank_teams.get(i), rank_teams.get(j), out])
            

if __name__ == '__main__':
    file = open("nba_ranks_data.csv")
    info = []
    data = csv.reader(file)
    # [0,2,4,5,6,7,8,9]
    for row in data:
        temp = []
        temp.append(row[0])
        temp.append(row[2])
        #[temp.append(row[x]) for x in range(4, 10)]
        wins = int(row[4]) + int(row[6])
        losses = int(row[5]) + int(row[7])
        temp.append(wins)
        temp.append(losses)
        temp.append(wins / (wins+ losses))
        temp.append(row[-1])
        info.append(temp)
    file2 = open('test_data.csv')
    data2 = csv.reader(file2)
    info2 = []
    for t in data2:
        info2.append(t)
    #neuralNet(info, info2)
    test('filename5.xml', info2)
    
    