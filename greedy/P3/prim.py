# Your task is to run Prim's minimum spanning tree algorithm on this graph.  You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below. 

# IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs).  The superior approach stores the unprocessed vertices in the heap, as described in lecture.  Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.

import sys 
from edgeWeightedGraph import EdgeWeightedGraph
from minPQ import MinPQ

class LazyPrimMST:
    def __init__(self, G):
        self._pq = MinPQ(G.countV())
        self._marked = dict()
        for v in G.vertices():
            self._marked[v] = False
        self._mst = []

        self.visit(G, '1')
        while not self._pq.isEmpty():
            e = self._pq.delRoot()
            v = e.either()
            w = e.other(v)
            if self._marked[v] and self._marked[w]: continue
            self._mst.append(e)
            if not self._marked[v]: self.visit(G, v)
            if not self._marked[w]: self.visit(G, w)

    def visit(self, G, v):
        self._marked[v] = True 
        for e in G.adj(v):
            if not self._marked[e.other(v)]: self._pq.insert(e) 
    
    def edges(self):
        return self._mst

    def weight(self):
        cost = 0
        for e in self.edges():
            cost += e.weight()
        return cost

def main():
    file = sys.argv[1]
    G = EdgeWeightedGraph(file)
    print(G)
    minST = LazyPrimMST(G)
    # cost = minST.cost()
    # print(cost)
    print(20*'=')
    for e in minST.edges():
        print(e)
    print(20*'=')
    print(minST.weight())
    

if __name__ == '__main__':
    main()


# -3612829