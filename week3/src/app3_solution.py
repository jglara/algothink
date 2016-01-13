'''
Created on Oct 21, 2015

@author: ejogarv
'''
import random
from Cluster import Cluster
import time
from alg_project3_solution import hierarchical_clustering, kmeans_clustering
import alg_project3_solution
from matplotlib.pyplot import plot, show, ylabel, xlabel, xscale, yscale, title
from matplotlib.pyplot import legend
import urllib2


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] 
            for tokens in data_tokens]

def gen_random_clusters(num_clusters):
    return [Cluster(set([]), random.uniform(-1,1), random.uniform(-1,1), 1,0) for _ in range(0,num_clusters)]

def plot_running_times():
    slow_measures = []
    #slow_measures.append(time.clock())
    last_time = time.clock()
    for size_cluster in range(2,200):        
        alg_project3_solution.slow_closest_pair(gen_random_clusters(size_cluster))
        slow_measures.append(time.clock() - last_time)
        last_time = time.clock()
            
    fast_measures = []
    #fast_measures.append(time.clock())  
    last_time = time.clock()  
    for size_cluster in range(2,200):        
        alg_project3_solution.fast_closest_pair(gen_random_clusters(size_cluster))
        fast_measures.append(time.clock() - last_time)
        last_time = time.clock()
        
    xlabel("number of points in cluster")
    ylabel("running time")
    #xscale('log')
    #yscale('log')
    plot(range(2,200), fast_measures, '-b', label="fast_closest_pair")
    plot(range(2,200), slow_measures, '-r', label="slow_closest_pair")
    legend(loc="upper left")
    show()
    
def compute_distortion(cluster_list,data_table):
    return sum([clu.cluster_error(data_table) for clu in cluster_list])

    
    
def plot_distortions():
    DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
    DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
    DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
    DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
    DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"
    DATA_24_URL = DIRECTORY + "data_clustering/unifiedCancerData_24.csv"

    
        
    #cluster_list = sequential_clustering(singleton_list, 15)    
    #print "Displaying", len(cluster_list), "sequential clusters"

    data_table = load_data_table(DATA_896_URL)
    singleton_list = []
    for line in data_table:
        singleton_list.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    errors_h = []
    for num_clusters in range(6,21):             
        cluster_list = hierarchical_clustering([clu.copy() for clu in singleton_list], num_clusters)
        cluster_error = compute_distortion(cluster_list, data_table)
        errors_h.append(cluster_error)
        
    errors_k = []
    for num_clusters in range(6,21):             
        cluster_list = kmeans_clustering([clu.copy() for clu in singleton_list], num_clusters, 5)
        cluster_error = compute_distortion(cluster_list, data_table)
        errors_k.append(cluster_error)
        
    xlabel("number of output clusters")
    ylabel("distortion")
    #xscale('log')
    #yscale('log')
    plot(range(6,21), errors_h, '-b', label="hierarchical")
    plot(range(6,21), errors_k, '-r', label="kmeans")
    
    legend(loc="upper left")
    title("896 county data sets")
    show()
    
    
if __name__ == "__main__":
     plot_distortions()