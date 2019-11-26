# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:24:09 2019

@author: Luke
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:30:35 2019

@author: Luke
"""
import copy
from dimacs import *
import time
import os

 
 
class Graph:
 
    
    def __init__(self,gr):
        self.graph=[]
        self.V=gr[0]
        for i in range(self.V+1):
            self.graph.append({})
        for (x, y, w) in gr[1]:
            self.graph[x].update({y:w})
         
    def BFS(self,s, t, parent):
        
        visited=[False]*(self.V+1)
        queue=[]
       
        visited[s] = True
        queue.append(s)
       
        while queue:
            u = queue.pop(0)
            for key in self.graph[u]:
                val=self.graph[u][key]
                if visited[key] == False and val > 0 :
                    queue.append(key)
                    visited[key] = True
                    parent[key] = u
        return visited[t]
            
    def EdmondKarps(self, source, sink):
        g_copy =copy.deepcopy(self.graph)
        parent=[-1]*(self.V+1)
 
        max_flow = 0  
 
        while self.BFS(source, sink, parent):
            #print(parent[sink])
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow +=  path_flow
 
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                if u not in self.graph[v]:
                    self.graph[v].update({u:path_flow})
                else: self.graph[v][u] += path_flow
                v = parent[v]
        self.graph=g_copy
        return max_flow
    def edgeConnectivity(self):
        s=1
        maxi=0
        for t in range(2, self.V+1):
            maxi=max(maxi,self.EdmondKarps(s, t))
        return maxi

def run(f):
    gr = Graph(loadWeightedGraph(f))
    return gr.edgeConnectivity()   
  
  

#print(run('grafy/connectivity/clique200'))

files = os.listdir("grafy/connectivity")
for i in files:  
    res = -1
    with open('grafy/connectivity/' + i) as f:
        res = int(readSolution('grafy/connectivity/' + i))
    start = time.time()
    res_t = run('grafy/connectivity/' + i)
    end = time.time()
    if(res == res_t):
		print(i + ": OK")
    else:
		print(i + ":Poprawna odpowiedz: " + str(res) + " Odpowiedz algorytmu: " + str(res_t))
