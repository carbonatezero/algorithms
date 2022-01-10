#-----------------------------------------------------------------------
import sys
import stdio
from weightedEdge import WeightedEdge

class EdgeWeightedGraph:

    # Construct a new edgeWeightedGraph object. If a filename is 
    # specified, populate the EdgeWeightedGraph object by reading 
    # data from the specified file with the specified delimiter.
    def __init__(self, filename=None):
        self._v = 0         # number of vertices in this digraph
        self._e = 0         # number of edges in this digraph
        self._adj = dict()  # adj[v] = adjacency list for vertex v
        self._edges = []

        with open(filename,'r') as f:
            lines = f.readlines()
            line = lines[0].split()
            self._v = int(line[0])
            for i in range(1,len(lines)):
                line = lines[i].split()
                u, w = line[0], line[1]
                weight = int(line[2])
                e = WeightedEdge(u,w,weight)
                self.addEdge(e)
                
    def addEdge(self, e):
        v = e.either()
        w = e.other(v)

        if not self.hasVertex(v): self._adj[v] = set()
        if not self.hasVertex(w): self._adj[w] = set()
        if not self.hasEdge(e):
            self._e += 1
            self._adj[v].add(e)
            self._adj[w].add(e)
            self._edges.append(e)

    # Return True if vertex v is in self, and False otherwise.
    def hasVertex(self, v):
        return v in self._adj

    # Return True if e is an edge in self, and False otherwise.
    def hasEdge(self, e):
        v = e.either()
        return e in self._adj[v]
    
    # Return an iterable collection of all vertices in self.
    def vertices(self):
        return iter(self._adj)

    # Return an iterable collection of all weighted edges in self.
    def edges(self):
        return self._edges 

    # Return an iterable collection containing all edges from
    # vertex v in self.
    def adj(self, v):
        return iter(self._adj[v])

    # Return the number of vertices in self.
    def countV(self):
        return len(self._adj)

    # # Return a string representation of self.
    def __str__(self):
        s = ''
        # for v in self.vertices():
        #     for e in self.adj(v):
        #         w = e.other(v)
        #         s += '{:>2s} - {:>2s}: {:>5d}\n'.format(v,w,e.weight())
        
        for e in self.edges():
            v = e.either()
            w = e.other(v)
            s += '{:>2s} - {:>2s}: {:>5d}\n'.format(v,w,e.weight())
        return s

#-----------------------------------------------------------------------

# For testing. Accept string file as a command-line argument. Create a
# EdgeWeightedGraph object by reading from file. Write the 
# EdgeWeightedGraph object to standard output.

def main():
    file = sys.argv[1]
    G = EdgeWeightedGraph(file)
    stdio.writeln(G)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------