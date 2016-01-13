'''
Created on Sep 9, 2015
DPA algorithm

@author: jglara
'''

import random
#from citation import plot_citation_graph

def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete directed graph with the specified number of nodes
    '''
    digraph = {}
    for node in range(0,num_nodes):
        digraph[node] = set([x for x in range(0,num_nodes) if x != node])
    return digraph

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
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
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

def DPA(n_nodes, m_nodes):
    '''
    Returns a random directed graph generated with the DPA algorithm
     n_nodes is the number of nodes
     m_nodes is the number of existing nodes to which a new node is
     connected during each iteration (m<=n)
     '''

    # create the initial complete digraph with m_nodes
    digraph = make_complete_graph(m_nodes)

    dpa_trial = DPATrial(m_nodes)
    for i_node in range(m_nodes, n_nodes):
        # calculate sum of the indegrees ox existing nodes
        digraph[i_node] = dpa_trial.run_trial(m_nodes)

    return digraph

if __name__ == "__main__":
    dg = DPA(27770,13)
    #plot_citation_graph(dg, "dga_27770_13_dist", "DGA graph in degree distribution")
    
