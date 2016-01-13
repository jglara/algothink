'''
Created on Sep 30, 2015

@author: ejogarv
'''
from utils import load_graph, NETWORK_URL,random_ugraph, fast_targeted_order,\
    targeted_order
from UPA import UPA
from CC import compute_resilience
from random import shuffle
from matplotlib.pyplot import plot, show, ylabel, xlabel, xscale, yscale
from matplotlib.pyplot import legend
import time

def get_resilience(ugraph):
    nodes = ugraph.keys()
    shuffle(nodes)    
    cc_set = compute_resilience(ugraph, nodes)
    
    return cc_set

def get_resilience_targeted(ugraph):
    nodes = fast_targeted_order(ugraph)    
    cc_set = compute_resilience(ugraph, nodes)
    
    return cc_set

def show_graph_question_2():
    computer_graph = load_graph(NETWORK_URL)
    num_nodes = len(computer_graph.keys())
    
    prob = 0.02
    random_graph = random_ugraph(prob, num_nodes)
    
    m_nodes= 3
    up_graph = UPA(num_nodes, m_nodes)
    
    cg_set = get_resilience(computer_graph)
    rg_set = get_resilience(random_graph)
    up_set = get_resilience(up_graph)
    
    xlabel("Nodes removed")
    ylabel("Size of largest connect component")
    plot(range(0,len(cg_set)), cg_set, '-b', label="computer graph")
    plot(range(0,len(rg_set)), rg_set, '-r', label="random graph. p=0.02")
    plot(range(0,len(up_set)), up_set, '-g', label="UPA graph. m=3")
    
    #plot(range(0,1239), [0.75 * (1239 - x) for x in range(0,1239)])
    
    legend(loc="upper right")
    show()
    
def show_graph_question_3():
    
    # build the list of graphs
    graph_list= []
    for nodes in range(10, 1000,10):
        graph_list.append(UPA(nodes, 5))
        
    # compute targeted_order using fast algorithm
    fast_measures = []
    for graph in graph_list:
        fast_targeted_order(graph)
        fast_measures.append(time.clock())
        
    # do the same with the slow version of the algorithm
    slow_measures = []
    for graph in graph_list:
        targeted_order(graph)
        slow_measures.append(time.clock())
        
    xlabel("number of nodes")
    ylabel("running time")
    #xscale('log')
    #yscale('log')
    plot(range(10, 1000,10), fast_measures, '-b', label="fast_targeted_order")
    plot(range(10, 1000,10), slow_measures, '-r', label="targeted_order")
    legend(loc="upper left")
    show()
    
def show_graph_question_4():
    computer_graph = load_graph(NETWORK_URL)
    num_nodes = len(computer_graph.keys())
    
    prob = 0.02
    random_graph = random_ugraph(prob, num_nodes)
    
    m_nodes= 3
    up_graph = UPA(num_nodes, m_nodes)
    
    cg_set = get_resilience_targeted(computer_graph)
    rg_set = get_resilience_targeted(random_graph)
    up_set = get_resilience_targeted(up_graph)
    
    xlabel("Nodes removed")
    ylabel("Size of largest connect component")
    plot(range(0,len(cg_set)), cg_set, '-b', label="computer graph")
    plot(range(0,len(rg_set)), rg_set, '-r', label="random graph. p=0.02")
    plot(range(0,len(up_set)), up_set, '-g', label="UPA graph. m=3")
    
    #plot(range(0,1239), [0.75 * (1239 - x) for x in range(0,1239)])
    
    legend(loc="upper right")
    show()
    
    
    
if __name__ == "__main__":
     show_graph_question_4()   