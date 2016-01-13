'''
Degree distributions for graphs. Three specific graphs as constanst and two functions computing degree distibutions

@author: jglara
'''

EX_GRAPH0 = {0: set([1,2]),
             1: set([]),
             2: set([]) }

EX_GRAPH1 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}



def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete directed graph with the specified number of nodes
    '''
    digraph = {}
    for node in range(0,num_nodes):
        digraph[node] = set([x for x in range(0,num_nodes) if x != node])
    return digraph

def compute_in_degrees(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes
    the in-degrees for the nodes in the graph.
    Returns a dictionary with the same set of keys (nodes) as digraph
    whose corresponding values are the number of edges whose head matches a
    particular node.
    '''
    in_degrees = {}
    for node in digraph.keys():
        in_degrees[node] = 0

    for adj_list in digraph.itervalues():
        for node in adj_list:
            in_degrees[node] = in_degrees[node] + 1

    return in_degrees

def in_degree_distribution(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and
    computes the unnormalized distribution of the in-degrees of the graph
    The function should return a dictionary whose keys correspond to in-degrees
    of nodes in the graph.
    '''
    in_degrees = compute_in_degrees(digraph)
    degree_dist = {}
    for degree in in_degrees.values():
        if degree in degree_dist:
            degree_dist[degree] = degree_dist[degree]+1
        else:
            degree_dist[degree] = 1

    return degree_dist
