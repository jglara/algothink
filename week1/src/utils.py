'''
Created on Sep 30, 2015

@author: ejogarv
'''


# general imports
import urllib2
from random import random
from wx.lib import graphics

############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
    
def fast_targeted_order(ugraph):
    
    # degree_sets[k] is a ser of all nodes whose degree is k
    #degree_sets = dict([(n,set()) for n in ugraph.keys()])
    
    # copy the graph
    new_graph = copy_graph(ugraph)
       
    order_list = []
    
    # fill the sets
    degree_sets = dict([(n,set([])) for n in range(0, len(ugraph.keys())) ])
    for (node,neigh_set) in ugraph.iteritems():
        degree = len(neigh_set)    
        degree_sets[degree].add(node)
            
    for degree in sorted(degree_sets.keys(), reverse=True):
        # remove nodes from the set
        while len(degree_sets[degree]) > 0:
            
            node = degree_sets[degree].pop()
            # remove node and redjust degree_sets
            for neigh in new_graph[node]:
                neigh_degree = len(new_graph[neigh]) 
                degree_sets[neigh_degree].remove(neigh)
                new_graph[neigh].remove(node)
                degree_sets[neigh_degree - 1].add(neigh)
                
            new_graph.pop(node)
            order_list.append(node)
    
    return order_list
    
    

def random_ugraph(prob, num_nodes):
    ugraph = dict( (n,set()) for n in range(0,num_nodes-1))
    for i in range(0,num_nodes-1):
        for j in range(0,num_nodes-1):
            if i != j and random() < prob:
                ugraph[i].add(j)
                ugraph[j].add(i)
                
            #digraph[i] = set([n for n in range(0,num_nodes-1) if n != i and random() < prob])
    
    return ugraph

def get_num_edges(graph):
    return sum([len(neigh) for neigh in graph.itervalues()])

def get_edges_distribution(graph):
    return [len(neigh) for neigh in graph.itervalues()]


def random_order(graph):
    l= graph.keys()
    random.shuffle(l)
    return l
 

def is_undirected(graph):
    for node in graph:
        for neigh in graph[node]:
            if not node in graph[neigh]:
                return False            
    return True

##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph
