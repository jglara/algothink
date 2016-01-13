'''
Created on Oct 16, 2015

@author: ejogarv
'''



#####################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))



def slow_closest_pair(cluster_list):
    """ Takes a list of Cluster objects and returns a closest pair where 
        the pair is represented by the tuple (dist, idx1, idx2) with idx1 < idx2 where 
        dist is the distance between the closest pair cluster_list[idx1] and cluster_list[idx2]. 
        
        This function should implement the brute-force closest pair method
    """
    
    mindist = float('inf')
    minidx1 = -1
    minidx2 = -1
    
    for idx1 in range(0,len(cluster_list)):
        for idx2 in range(0,len(cluster_list)):
            if idx1 != idx2:
                (distance, pair_idx1, pair_idx2) = pair_distance(cluster_list,idx1,idx2)
                if distance < mindist:
                    mindist = distance
                    minidx1 = pair_idx1
                    minidx2 = pair_idx2
    
    #print("slow closest_pair: {0} d={1} i1={2} i={3}".format(cluster_list, mindist, minidx1,minidx2))
    return (mindist, minidx1, minidx2)

def fast_closest_pair(cluster_list):
    """ Takes a list of Cluster objects and returns a closest pair where 
        the pair is represented by the tuple (dist, idx1, idx2) with idx1 < idx2 where 
        dist is the distance between the closest pair cluster_list[idx1] and cluster_list[idx2]. 
        
        This function should implement the divide-and-conquer closest pair method
    """
    
    #print("fast closest_pair: {0}".format(cluster_list))
    # base case
    if len(cluster_list) <= 3:
        return slow_closest_pair(cluster_list)
    
    
    # first, order the cluster horizonatally
    cluster_list.sort(key = lambda cluster: cluster.horiz_center())
    
    # divide in two halfs, and apply recursion
    clusterlen = len(cluster_list)
    leftlen = (clusterlen / 2) + (clusterlen % 2)    
    mid = (cluster_list[leftlen-1].horiz_center() + cluster_list[leftlen].horiz_center()) / 2.0
                                                                                        
    (leftmin, leftidx1, leftidx2) = fast_closest_pair(cluster_list[:leftlen])
    (rightmin, rightidx1, rightidx2) = fast_closest_pair(cluster_list[leftlen:])
    rightidx1 = rightidx1+leftlen 
    rightidx2 = rightidx2+leftlen
    
    # for checking. rmove
    if False:
        (leftmin_, leftidx1_, leftidx2_) = slow_closest_pair(cluster_list[:leftlen])
        (rightmin_, rightidx1_, rightidx2_) = slow_closest_pair(cluster_list[leftlen:])
        rightidx1_ = rightidx1_+leftlen 
        rightidx2_ = rightidx2_+leftlen
        
        if (leftmin_, leftidx1_, leftidx2_) != (leftmin, leftidx1, leftidx2):
            print "ERROR 1"
        
        if (rightmin_, rightidx1_, rightidx2_) != (rightmin, rightidx1, rightidx2):
            print "ERROR 2"
        
    

    
    # get the closest pair in the strip
    (stripmin, stripidx1, stripidx2) = closest_pair_strip(cluster_list, mid, min(leftmin,rightmin))
    
    # return the min of three
    return min ((leftmin, leftidx1, leftidx2),
                (rightmin, rightidx1, rightidx2),
                (stripmin, stripidx1, stripidx2)
                )

def closest_pair_strip(cluster_list, horiz_center, half_width):
    """ Takes a list of Cluster objects and two floats horiz_center and half_width. 
    horiz_center specifies the horizontal position of the center line for a vertical strip. 
    half_width specifies the maximal distance of any point in the strip from the center line. 
    
    return a tuple corresponding to the closest pair of clusters that lie in the specified strip. 
    (Again the return pair of indices should be in ascending order.)
    """
    
    #print("closest_pair_strip: " + str(cluster_list) + " " + str(horiz_center) + " " + str(half_width))
    
    mindist = float('inf')
    minidx1 = -1
    minidx2 = -1
    
    # filter the cluster_list to have only cluster in the strip
    strip_idx = [(i, cluster) for i,cluster in enumerate(cluster_list) if abs(cluster.horiz_center() - horiz_center) <= half_width ]
    if (len(strip_idx) == 0):
        return (mindist,minidx1,minidx2)
    
    # order strip vertically
    strip_idx.sort(key = lambda (_,cluster): cluster.vert_center())
    
    # check mindist. For every element, we only have to check next three
    idxs,strip = zip(*strip_idx)
    
    striplen = len(strip)
    for idx1 in range(0,striplen):
        for idx2 in range(idx1+1, min(striplen, idx1+4)):
            (distance, pair_idx1, pair_idx2) = pair_distance(strip,idx1,idx2)
            if distance < mindist:
                mindist = distance
                minidx1 = pair_idx1
                minidx2 = pair_idx2
    
    #print("Found: " + str(mindist) + " " + str(idxs[minidx1]) + " " + str(idxs[minidx2]))
    return (mindist, min(idxs[minidx1], idxs[minidx2]), max(idxs[minidx1], idxs[minidx2]))


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    
    while len(cluster_list) > num_clusters:
        (_,idx1,idx2) = fast_closest_pair(cluster_list)
        cluster_list[idx1].merge_clusters(cluster_list[idx2])
        del cluster_list[idx2]

    return cluster_list

######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations    
    core_clusters =  sorted(cluster_list,key= lambda cluster: cluster.total_population(),reverse=True)[:num_clusters]
    
    clusters_map = []
    for _ in range(0,num_iterations):
        clusters_map = [None] * num_clusters
        # merge each cluster with the nearest one
        for cluster in cluster_list:
            (idx, _) = min( enumerate(core_clusters), key=lambda (_,clu): clu.distance(cluster))
            if (clusters_map[idx] != None):
                clusters_map[idx].merge_clusters(cluster.copy())
            else:
                clusters_map[idx] = cluster.copy()
                       
        # recreate core_cluster with the cluster centers
        core_clusters = [clu.copy() for clu in clusters_map]
            
    return clusters_map

