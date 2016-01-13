'''
Created on Sep 8, 2015

@author: jglara
'''
from random import random


def random_digraph(prob, num_nodes):
    digraph = dict( (n,set()) for n in range(0,num_nodes-1))
    for i in range(0,num_nodes-1):
        for j in range(0,num_nodes-1):
            if i != j and random() < prob:
                digraph[i].add(j)
            if i != j and random() < prob:
                digraph[j].add(i)
                
            #digraph[i] = set([n for n in range(0,num_nodes-1) if n != i and random() < prob])
    
    return digraph
    
def random_ugraph(prob, num_nodes):
    ugraph = dict( (n,set()) for n in range(0,num_nodes-1))
    for i in range(0,num_nodes-1):
        for j in range(0,num_nodes-1):
            if i != j and random() < prob:
                ugraph[i].add(j)
                ugraph[j].add(i)
                
            #digraph[i] = set([n for n in range(0,num_nodes-1) if n != i and random() < prob])
    
    return ugraph