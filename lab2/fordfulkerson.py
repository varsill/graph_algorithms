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
   
   
    def DFS( self, s,t, parent ):   # DFS w grafie G z wierzchołka s
        visited = [False] * (self.V+1)
        for i in range(1, self.V+1):
            if not visited[i]:
                self.DFSVisit(i, visited, parent)
        return visited[t]


    def DFSVisit(self, i, visited, parent ):  # rekurencyjna funkcja realizująca DFS
        visited[i] = True
        for key in self.graph[i]:
            val=self.graph[i][key]
            if visited[key]==False and val>0:
                parent[key]=i
                self.DFSVisit(key, visited, parent)              
   
    def FordFulkerson(self, source, sink, fun):
        g_copy =copy.deepcopy(self.graph)
        parent=[-1]*(self.V+1)
 
        max_flow = 0  
 
        while fun(source, sink, parent):
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
            maxi=max(maxi,self.FordFulkerson(s, t, g.BFS))
        return maxi
def run(f):
    gr = Graph(loadWeightedGraph(f))
    return gr.FordFulkerson(1, gr.V, gr.DFS)   
  
  
files = os.listdir("grafy/flow")
for i in files:  
    res = -1
    with open('grafy/flow/' + i) as f:
        res = int(readSolution('grafy/flow/' + i))
    start = time.time()
    res_t = run('grafy/flow/' + i)
    end = time.time()
    if(res == res_t):
		print(i + ": OK")
    else:
		print(i + ": Poprawna odpowiedz: " + str(res) + " Odpowiedz algorytmu: " + str(res_t))
    #print('(%f)' % (end-start))