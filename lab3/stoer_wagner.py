from dimacs import *
from Queue import PriorityQueue
import time 
import os
import copy
class Graph:
 
    def __init__(self,gr):
        self.graph=[]
        self.V=gr[0]
        for i in range(self.V+1):
            self.graph.append({})
        for (x, y, w) in gr[1]:
            self.graph[x].update({y:w})
            self.graph[y].update({x:w})

    def get_min_cut(self):
        graph_copy=copy.deepcopy(self.graph)
    	W = [0]*(self.V+1)
    	visited = [False] * (self.V+1)
    
    	Q = PriorityQueue()
    	Q.put((0, 1))
    
    	L = []
    
    	while(not Q.empty()):
    		w, v = Q.get()
    		w = -w
    		if(not visited[v]):
    			L.append(v)
    			visited[v] = True
    			for (u, w) in self.graph[v].items():
    				if(not visited[u]):
    					W[u] += w
    					Q.put((-W[u], u))

    	a = L[-1]
    	b = L[-2]
    
    	res = 0
    	for (i,weight) in self.graph[a].items(): res += weight
    	self.merge(b, a)
        self.graph=graph_copy
    	return res
    
    def merge(self, x, y ):
    	neighbours = list(self.graph[y].items())
    	for (i, w) in neighbours:
            del self.graph[y][i]
            del self.graph[i][y]
            if i != x:
                if self.graph[x][i] is not None: self.graph[y].update({i:self.graph[x][i]+w})
                else: self.graph[x].update({i:w})
                if self.graph[i][x] is not None: self.graph[i].update({x:self.graph[i][x]+w})
                else: self.graph[i].update({x:w})

def run(file_name):
    G = Graph(loadDirectedWeightedGraph(file_name))
    res = float("inf")
    i=G.V
    while(i > 1):
        i -= 1
        res = min(res, G.get_min_cut())
    return res



PATH = "grafy/connectivity/"
files = os.listdir(PATH)
for i in files:  
    res = -1
    with open(PATH + i) as f:
        res = int(readSolution(PATH + i))
    start = time.time()
    res_t = run(PATH + i)
    end = time.time()
    if(res == res_t):
		print(i + ": OK")
    else:
		print(i + ":Poprawna odpowiedz: " + str(res) + " Odpowiedz algorytmu: " + str(res_t))
