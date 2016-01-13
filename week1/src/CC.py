'''
Created on Sep 23, 2015

@author: ejogarv
'''
from collections import deque


def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node
    and returns the set consisting of all nodes that are visited
    by a breadth-first search that starts at start_node.
    """
    
    visited = set([start_node])
    cola = deque([start_node])
    
    while len(cola)>0:
        node = cola.popleft()        
        for neigh in ugraph[node]:
            if not neigh in visited:
                visited.add(neigh)
                cola.append(neigh)
    
    return visited

def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets, where
    each set consists of all the nodes (and nothing else) in a connected
    component, and there is exactly one set in the list for each connected
    component in ugraph and nothing else.
    """
    
    remaining = set(ugraph.keys())
    ccomp = []
    while len(remaining) > 0:
        node = remaining.pop()
        visited = bfs_visited(ugraph,node)
        ccomp.append(visited)
        remaining.difference_update(visited)
        
    return ccomp
    
def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer) of 
    the largest connected component in ugraph.
    """
    ccomp = cc_visited(ugraph)
    if len(ccomp) == 0:
        return 0
        
    return max([len(s) for s in ccomp])

def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order and iterates 
    through the nodes in attack_order. For each node in the list, the function 
    removes the given node and its edges from the graph and then computes the
    size of the largest connected component for the resulting graph.
    """
    
    resilience_list = [largest_cc_size(ugraph)]
    for node in attack_order:
        # remove node and edges
        for neigh in ugraph[node]:
            ugraph[neigh].discard(node)
        ugraph.pop(node)
        resilience_list.append(largest_cc_size(ugraph))
        
    return resilience_list
    

    