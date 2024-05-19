from math import inf
import sys


#ask for file, open it, and store into a list
#input = input("Enter file name: \n")
file = open('data/RomaniaVertices.txt', "r")
text = file.readlines()
text.pop(0)
Cities = []
for i in range(len(text)):
    text[i] = text[i].rstrip("\n")
   # text[i] = text[i].split(",")
   #text[i] = int(text[i])
    Cities.append(text[i])
print("Cities:")
print(Cities)
print("\n")

file = open('data/RomaniaEdges.txt', "r")
text = file.readlines()
text.pop(0)
Edges = []
for i in range(len(text)):
    text[i] = text[i].rstrip("\n")
    text[i] = text[i].split(",")
    #text[i] = str(text[i])
    Edges.append(text[i])
print("Edges:")
print(Edges)
print("\n")


v = Cities
vLength = len(v)
eLength = len(Edges)


#### Breadth First Search ####
def BFS(A, s, d):
    
    visited = []

    #create queue
    queue = [[s]]
    
    if s == d:
        print("source node")
        return
    
    #traversal loop
    while queue:
        path = queue.pop()
        node = path[-1]

        #visited??
        if node not in visited:
            neighbors = A[node]

            for n in neighbors:
                newPath = list(path)
                newPath.append(n)
                queue.append(newPath)
                #check if n is destination
                if n == d:
                    print("Shortest Path:", *newPath)
                    return
            visited.append(node)
    

   
from collections import defaultdict


## graph class
class Graph:
    def __init__(A):
        A.dict = defaultdict(list)
    
    #add edges to graph
    def add_edge(A, src, dest, wght):
        A.dict[src].append(dest)
        A.dict[dest].append(src)
    



class minHeap:
#initialize min heap
    def __init__(A, capacity):
        A.capacity = capacity 
        A.size = 0
        A.heap = [0]*(A.capacity + 1)
        A.heap[0] = -1* sys.capacity
        A.parent = 1
        A.root = 1
# create parent-Children relations
    def Parent(A, i):
        return (i-1)//2
    def Left(A, i):
        return 2*i + 1
    def Right(A, i):
        return 2*i + 2

    def hasParent(A, i):
        return A.getParent(i) >= 0
    

    
#### Implement a priority queue using a binary heap ####
def min_Heapify(A, i):
    l = 2*i + 1
    r = 2*i + 2
    if l <= A.heapSize and A[l] < A[i]:
        lowest = l
    else:
         lowest = i
    if r <= A.heap_size and A[r] < A[lowest]:
        lowest = r
    if lowest != i:
        temp = A[i]
        A[i] = A[lowest]
        A[lowest] = temp
        min_Heapify(A, lowest)

def buildMin(A):
    A.heap_size = A.length
    for i in range(A.length//2, 0): #might be 0
        min_Heapify(A, i)

def heapsort(A): 
    for i in range(A.length, 1): #might be 2
        temp = A[i]
        A[i] = A[1]
        A[1] = temp
        A.heapSize = A.heapSize - 1
        min_Heapify(A, 1)

def extractMin(A):
    if (A.heapSize == 0):
        raise "heap is empty"
    min = A[0]
    A[0] = A[A.heapSize - 1]
    A.heapSize -= 1
    min_Heapify(A,1)
    return min


#decrease key
def decreaseKey(A, i, key):
    if key > A[i]:
        raise("new key is larger than current key")
    A[i] = key
    while i < A.heapSize and A[key.Parent(i)] < A[i]:
        temp = A[i]
        A[i] = A[key.Parent(i)]
        A[key.Parent(i)] = temp

def insert(A, key):
    A.heapSize += 1
    A[A.heapSize] = inf
    decreaseKey(A, A.heapSize, key) 



#### Dijkstra's algorithm ####

def Dijkstra(A, s, v):
    initSS(A,s)
    S = []
    Q = minHeap(len(v)+1)
    for i in v:
        insert(Q,i)
    while Q.size != None:
        u = extractMin(Q)
        S = S.union(u)
        for v in A.Adj[u]:
            Relax(u,v[0],v[1],Q)
    

def Relax(u, v, w, Q):
    if v.d > u.d + w:
        v.d = u.d + w #decrease key
        v.pi = u
    for i in range(Q.size):
        index = Q.front + i
        if Q.heap[index] == v:
            decreaseKey(Q, index, v.d)

def initSS(G,s):
    for v in G:
        if v.key != s:
            v.d = 1000000000
            v.pi = None
        else:
            v.d = 0
    s.d = 0


#### Bonus: Prim's Algorithm ####
# once implemented, print spanning tree by printing full predecessor structure 
'''def Prim(G, w, r):
    for each u in G.V:
        u.key = inf
        u.pi = NIL
    r.key = 0
    Q = G.V
    while Q != None :
        u = extract_min(Q)
        for each v in G.Adj[u]:
            if v in Q and w(u,v) < v.key:
                v.pi = u
                v.key = w(u,v)'''

#driver for element 
if __name__ == "__main__":
    graph = Graph()  

    for i in range(0, eLength):
        element = Edges[i]

        source = element[0]
        dest = element[1]
        wght = element[2]
        graph.add_edge(source, dest, wght)
    
    print('Dictionary:', graph.dict)
    BFS(graph.dict, 'Arad', 'Sibiu')
    BFS(graph.dict, 'Arad', 'Craiova')
    BFS(graph.dict, 'Arad', 'Bucharest')
    
    
    Dijkstra(graph.dict, wght, 'Arad')