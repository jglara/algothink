'''
Created on Sep 9, 2015
UPA algorithm

@author: jglara
'''
import random
from compiler.ast import nodes


def make_complete_ugraph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete undirected graph with the specified number of nodes
    '''
    ugraph = {}
    for node in range(0,num_nodes):
        ugraph[node] = set([x for x in range(0,num_nodes) if x != node])
    return ugraph


class UPATrial:
    """
    Simple class to encapsulate optimized trials for UPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    


def UPA(n_nodes, m_nodes):
    '''
    Returns a random directed graph generated with the UPA algorithm
     n_nodes is the number of nodes
     m_nodes is the number of existing nodes to which a new node is
     connected during each iteration (m<=n)
     '''

    # create the initial complete digraph with m_nodes
    ugraph = make_complete_ugraph(m_nodes)

    UPA_trial = UPATrial(m_nodes)
    for i_node in range(m_nodes, n_nodes):
        # calculate sum of the indegrees ox existing nodes
        nodes= UPA_trial.run_trial(m_nodes)
        ugraph[i_node] = nodes
        for n in nodes:
            ugraph[n].add(i_node)

    return ugraph

if __name__ == "__main__":
    ug = UPA(27770,13)
    
