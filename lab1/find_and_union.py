from dimacs import *
import time
import os


def union(parents, x, y, ):
	a = find(parents, x)
	b = find(parents, y)

	if a is not b: parents[a] = b

def find(parents, x):
	if(parents[x] != x):
		v = parents[x]
		parents[x]=find(parents, v)
		return parents[x]
	else: return x

def run(file):
	(V, L) = loadWeightedGraph(file)

	L.sort(key=lambda x: x[2], reverse=True)

	s = 1
	t = 2

	parents = {i:i for i in range(1, V+1)}

	m = -1
	for (x, y, c) in L:
		union(parents, x, y)
		if(find(parents, s) == find(parents, t)):
			m=c
			break
	return m

files = os.listdir("grafy")
for i in files:  
    res = -1
    with open('grafy/' + i) as f:
        res = int(readSolution('grafy/' + i))
    start = time.time()
    res_t = run('grafy/' + i)
    end = time.time()
    if(res == res_t):
		print(i + ": OK")
    else:
		print(i + ": Poprawna odpowiedz: " + str(res) + " Odpowiedz algorytmu: " + str(res_t))
    #print('(%f)' % (end-start))
