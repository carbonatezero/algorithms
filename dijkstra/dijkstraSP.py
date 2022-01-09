import sys
import stdio
from indexMinPQ import IndexMinPQ
from edgeWeightedDigraph import EdgeWeightedDigraph

POSITIVE_INFINITY = float('inf')

class DijkstraSP:

    '''
    Computes a shortest-paths tree from the source vertex s to every other vertex
    in the edge-weighted digralph G
    G the edge-weighted digraph
    s the source vertex

    '''
    def __init__(self, G, s):
        self._edgeTo = dict() # _edgeTo[v] = last edge on shortest s->v path
        self._edgeTo[s] = None
        self._distTo = dict() # _distTo[v] = distance  of shortest s->v path
        self._pq = IndexMinPQ(G.countV()) # priority queue of vertices

        for v in G.vertices():
            self._distTo[v] = POSITIVE_INFINITY
        self._distTo[s] = 0.0
        
        # relax vertices in order of distance from s
        self._pq.insert(s, 0.0)
        while self._pq.isEmpty() is not True:
            self._relax(G, self._pq.delMin())

    def _relax(self, G, v): 
        for e in G.adj(v):
            w = e.edge_to()
            if self._distTo[w] > self._distTo[v] + e.weight():
                self._distTo[w] = self._distTo[v] + e.weight()
                self._edgeTo[w] = e
                if self._pq.contains(w): 
                    self._pq.change(w, self._distTo[w])
                else:
                    self._pq.insert(w, self._distTo[w])


    def distTo(self,v): 
        return self._distTo[v]
    
    def hasPathTo(self, v): 
        return self._distTo[v] < POSITIVE_INFINITY 
    
    def pathTo(self, v): 
        if not self.hasPathTo(v): return None 
        path = []
        e = self._edgeTo[v]
        while e is not None:
            path.append(e)
            e = self._edgeTo[e.edge_from()] 
        return reversed(path)

def main():
    # print(POSITIVE_INFINITY) 
    file = sys.argv[1]
    G = EdgeWeightedDigraph(file)
    print("graph:")
    print(G)

    s = sys.argv[2]
    print("source: {}".format(s))

    sp  = DijkstraSP(G, s)

    print("DijkstraSP:")
    
    report_vertices = G.vertices()
    a = [7,37,59,82,99,115,133,165,188,197]
    report_vertices = [str(i) for i in a]

    for t in report_vertices:
        if sp.hasPathTo(t):
            print("{} to {} ({:.0f})  ".format(s,t,sp.distTo(t)))
            for e in sp.pathTo(t):
                print("{}   ".format(e), end = "")
            stdio.writeln()
        else:
            print("{} to {}    no path".format(s,t))

    for t in report_vertices:
        if sp.hasPathTo(t):
            print("{},".format(int(sp.distTo(t))), end="")
    stdio.writeln()

if __name__ == '__main__':
    main()

