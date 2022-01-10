# Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4.  What is the maximum spacing of a 4-clustering?

# 11.10.21 Wed 
# next steps: write the G.edges() method and test it;
#             sort the weighted edges by the weights

# 11.11.21 Thu
# - G.edges() done;
# - sorting edges done;
# - the union find data structure written and tested
# - found the spacing function of k-cluster in the class notes (it's not in the book)
# - debug the spacing part of the code; bug fixed after adding the following condition:
#   not uf.connected(int(p)-1,int(q)-1)
# - tinycluster.txt is a good test example!


from edgeWeightedGraph import EdgeWeightedGraph
import sys 

from unionFind import UnionFind

class KruskalCluster:
    def __init__(self,G,k):
        self._T = []
        self._spacing = float('inf')
        n = G.countV()
        uf = UnionFind(n)
        E = sorted(G.edges())
        # print(40*'-')
        # for e in E:
        #     print(e)
        # print(40*'-')

        # for each (v,w) in E in nondecreasing order of cost
        for e in E:
            # print(e)
            if uf.count() <= k: break
            v = e.either()
            w = e.other(v)
            if not uf.connected(int(v)-1,int(w)-1):
                self._T.append(e)
                uf.union(int(v)-1,int(w)-1)
        print(40*'-')
        assert len(self._T) + uf.count() == n

        # print(40*'-')
        # for e in self._T:
        #     print(e)
        # print(40*'-')

        for e in E:
            if e in self._T: continue
            else:
                p = e.either()
                q = e.other(p)
                if  not uf.connected(int(p)-1,int(q)-1) 
                    and e.weight() < self._spacing:
                    self._spacing = e.weight()

    def maxSpacing(self):
        return self._spacing

def main():
    # prompt = "Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4.  What is the maximum spacing of a 4-clustering?" (soln found: 106)
    # print(prompt)
    file = sys.argv[1]
    G = EdgeWeightedGraph(file)
    # print(G)

    k = G.countV()
    k = 4
    soln = KruskalCluster(G,k)
    dist = soln.maxSpacing()
    print('max spacing of the {}-clustering:'.format(k))
    print(dist)


if __name__ == '__main__':
    main()