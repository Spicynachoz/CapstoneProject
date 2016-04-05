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

import data_extract

def neuralNet(info):
    ann = FeedForwardNetwork()
    
    '''
        Initiate the input nodes, hidden layer nodes,
        and the output layer nodes.
    '''
    inputLayer = LinearLayer(6)
    hiddenLayer = SigmoidLayer(3) 
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
    
    data_set = SupervisedDataSet(6, 1)
    '''
        Sample training set for knicks vs other teams
    '''
    for data in info:
        data_set.addSample(data[4:len(data)-2], data[len(data)-1])
    trainer = BackpropTrainer(ann, data_set)
    
    '''
        Using 50 epochs for testing purposes, it will train
        the network until convergence within the first 50 epochs
    
    '''
    trainer.trainUntilConvergence(dataset=data_set, maxEpochs=50)
    out = ann.activateOnDataset(data_set)
    print (out)

if __name__ == '__main__':
    info = data_extract.extractData("nba_data.csv")
    neuralNet(info)
    