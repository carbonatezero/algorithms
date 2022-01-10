# translated from https://algs4.cs.princeton.edu/15uf/UF.java.html

import stdio

class UnionFind:
    # initialize n sites with integer names (0 to n-1)
    def __init__(self,n):
        self._parent = [i for i in range(n)]
        self._rank   = [0 for i in range(n)]
        self._count  = n

    # add connection between p and q
    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return

        if   self._rank[rootP] < self._rank[rootQ]: self._parent[rootP] = rootQ
        elif self._rank[rootP] > self._rank[rootQ]: self._parent[rootQ] = rootP
        else: 
            self._parent[rootQ] = rootP 
            self._rank[rootP] += 1
        self._count -= 1

    # component identifier for p
    def find(self,p):
        self._validate(p)
        while p != self._parent[p]:
            self._parent[p] = self._parent[self._parent[p]]
            p = self._parent[p]
        return p

    # return true if p and q are in the same component
    def connected(self,p,q):
        return self.find(p) == self.find(q) 
    
    # number of components
    def count(self):
        return self._count 

    def _validate(self, p):
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError("index {} is not between 0 and {}".format(p,n-1))

def main():
        n = stdio.readInt()
        uf = UnionFind(n)
        while (not stdio.isEmpty()):
            p = stdio.readInt()
            q = stdio.readInt()
            if (uf.find(p) == uf.find(q)): continue
            uf.union(p, q)
            stdio.writeln(str(p) + " " + str(q))
        
        stdio.writeln(str(uf.count()) + " components");

if __name__ == '__main__':
    main()