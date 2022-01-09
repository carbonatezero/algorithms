#-----------------------------------------------------------------------
# edgeWeightedDigraph.py
#-----------------------------------------------------------------------

import sys
import stdio
from instream import InStream
from directedEdge import DirectedEdge

#-----------------------------------------------------------------------

class EdgeWeightedDigraph:

    # Construct a new edgeWeightedDigraph object. If a filename is 
    # specified, populate the EdgeWeightedDigraph object by reading 
    # data from the specified file with the specified delimiter.
    def __init__(self, filename=None, delimiter=None):
        self._v = 0         # number of vertices in this digraph
        self._e = 0         # number of edges in this digraph
        self._adj = dict()  # adj[v] = adjacency list for vertex v

        if filename is not None:
            instream = InStream(filename)
            while instream.hasNextLine():
                line = instream.readLine()
                names = line.split(delimiter)
                v = names[0]
                for i in range(1, len(names)):
                    temp   = names[i].split(',')
                    w      = temp[0]
                    weight = float(temp[1])
                    self.addEdge(DirectedEdge(v,w,weight))
                
    def addEdge(self, e):
        v = e.edge_from()
        w = e.edge_to()

        if not self.hasVertex(v): self._adj[v] = set()
        if not self.hasVertex(w): self._adj[w] = set()
        if not self.hasEdge(e):
            self._adj[v].add(e)
            self._e += 1

    # Return True if vertex v is in self, and False otherwise.
    def hasVertex(self, v):
        return v in self._adj

    # Return True if e is an edge in self, and False otherwise.
    def hasEdge(self, e):
        v = e.edge_from()
        return e in self._adj[v]
    
    # Return an iterable collection of all vertices in self.
    def vertices(self):
        return iter(self._adj)

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
        for v in self.vertices():
            for e in self.adj(v):
                w = e.edge_to()
                s += '{:>3s} -> {:>3s}: {}\n'.format(v,w,e.weight())
        return s

#-----------------------------------------------------------------------

# For testing. Accept string file as a command-line argument. Create a
# EdgeWeightedDigraph object by reading from file. Write the 
# EdgeWeightedDigraph object to standard output.

def main():
    file = sys.argv[1]
    G = EdgeWeightedDigraph(file)
    stdio.writeln(G)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

