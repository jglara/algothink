'''
Created on Nov 20, 2015

@author: ejogarv
'''
from string import lowercase

def printDistTo(DG, distTo):
    print " ".join(["%d" % (distTo[c]) for c in sorted(DG.keys())])
    

def relaxEdge(distTo, v, e):
    (w, weight) = e
    
    if (distTo[w] > distTo[v] + weight):
        distTo[w] = distTo[v] + weight
        
def relaxVertex(DG, distTo, v):
    if DG.has_key(v):
        for e in DG[v]:
            relaxEdge(distTo, v, e)
        
def selectNextVertexToRelax(distTo, relaxed):
    min_d = 10000
    min_v = ''
    for (v,d) in distTo.iteritems():
        if (d < min_d) and (v not in relaxed):
            min_d = d
            min_v = v
            
    return min_v 
        
def run_dijsktra(DG, initial):
    distTo =dict(zip(DG.keys(), [10000 for k in DG.keys()]))
    distTo[initial] = 0
    relaxed = []
    
    while len(relaxed) < 8:
        v = selectNextVertexToRelax(distTo, relaxed)
        print "Relaxing " + v
        relaxVertex(DG,distTo, v)
        printDistTo(DG, distTo)
        relaxed.append(v)

def run_topological(DG, order):
    distTo =dict(zip(DG.keys(), [10000 for k in DG.keys()]))
    distTo[order[0]] = 0
    
    for v in order:
        print "Relaxing " + v
        relaxVertex(DG,distTo, v)
        printDistTo(DG, distTo)
        
def run_bellmanford(DG, initial):
    distTo =dict(zip(DG.keys(), [10000 for k in DG.keys()]))
    distTo[initial] = 0
    
    for i in range(0,len(DG.keys())):
        print "Relaxing iter: %d" % i
        for v in sorted(DG.keys()):
            relaxVertex(DG,distTo,v)
        printDistTo(DG, distTo)
    

if __name__ == "__main__":
    DG_1 = {'a': [],
          'b': [('a', 24), 
                ('c', 34),
                ('f', 5),
                ('g', 69)],
          'c': [('d',30),
                ('g', 26),
                ('h', 47)],
          'd': [],
          'e': [('a', 43),
                ('b', 9),
                ('f', 22)],
          'f': [],
          'g': [('f',4),
                 ('h',20)],
          'h': [('d', 2)]}
    
    DG_2 = {'a': [],
            'b': [('a', 0),
                  ('e', 5)],
            'c': [('b',3)],
            'd': [('c',29)],
            'e': [('a',5)],
            'f': [('b',26),
                  ('e',15)],
            'g': [('b',52),
                  ('c',71),
                  ('d',41),
                  ('f',22),
                  ('h',28)],
            'h': [('d', 11)]
            }
    
    DG_3 = {'a' : [('b', 1)],
            'b': [('f', 19),
                  ('e', 41)],
            'c': [('d', 15),
                  ('b', 22),
                  ('f', 47)],
            'd': [],
            'e': [('a',30)],
            'f': [('e', 20)],
            'g': [('h',39),
                  ('f',54),
                  ('c',4)],
            'h': [('c',5),
                  ('d', 1)]}
    
    #run_dijsktra(DG_1, 'e')
    #run_topological(DG_2, "ghfdcbea")
    run_bellmanford(DG_3, 'g')