"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
from graph_degree import in_degree_distribution
from matplotlib.pyplot import plot, xlabel, ylabel, title, grid, show, savefig,\
    scatter, gca, xscale, yscale
import math
from random_graph import random_digraph

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

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

def plot_citation_graph(citation_graph, filename, plot_title):
    # find the indegree_distribution
    indeg_dist = in_degree_distribution(citation_graph)    
    # sort freq by keys
    number_citations = sorted(indeg_dist.keys())
    indeg_freq = [indeg_dist[n] for n in number_citations]

    # normalize
    total = sum(indeg_freq)
    indeg_freq_norm = [freq / float(total) for freq in indeg_freq]
    
    # calculate log/log, except for the first one (0)
    #log_number_citations = [math.log10(x) for x in number_citations[1:]]
    #log_indeg_freq_norm = [math.log10(x) for x in indeg_freq_norm[1:]]
    
    plot(number_citations[1:], indeg_freq_norm[1:], 'o')
    
    xscale("log")
    yscale("log")
    
    xlabel("log10 #citations")
    ylabel("log10 Norm.Freq.")
    title(plot_title)
    grid(True)
    savefig(filename)
    show()



if __name__ == "__main__":

    citation_graph = load_graph(CITATION_URL)
    plot_citation_graph(citation_graph, "citation_q1.png", "in-degree distribution of citations")
    
    total_citations = 352768.0
    total_papers = 27770.0
    med_cit_per_paper = ( total_citations / total_papers)
 
    dg = random_digraph(med_cit_per_paper / total_papers, 5000)
    #plot_citation_graph(dg,"/tmp/kk.png", "ER in-degree distribution")


