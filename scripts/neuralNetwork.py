# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:36:29 2016

@author: htanwar
"""

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import TanhLayer
from pybrain.structure import FullConnection
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
import os
import numpy as np

def neuralNet():
    ann = FeedForwardNetwork()
    
    '''
        Initiate the input nodes, hidden layer nodes,
        and the output layer nodes.
    '''
    inputLayer = LinearLayer(7)
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
    
    net = buildNetwork(7, 3, 1, bias = True, hiddenclass=TanhLayer)
    data = SupervisedDataSet(7, 1)
    '''
        Sample training set for knicks vs other teams
    '''
    data.addSample((7, 34, 10, 31, 0.17073170731707318, 0.24390243902439024, 22), (1))
    data.addSample((7, 34, 10, 30, 0.17073170731707318, 0.25, 4), (0))
    data.addSample((5, 34, 10, 30, 0.1282051282051282, 0.25, 8), (1))
    trainer = BackpropTrainer(ann, data)
    print(trainer.train())

if __name__ == '__main__':
    neuralNet()
    