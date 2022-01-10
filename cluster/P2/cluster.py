# The format is:

# [# of nodes] [# of bits for each node's label]

# [first bit of node 1] ... [last bit of node 1]

# [first bit of node 2] ... [last bit of node 2]

# ...

# For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

# The distance between two nodes u and v in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels.  For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

# The question is: what is the largest value of k such that there is a k-clustering with spacing at least 3?  That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?

# NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost.  So you will have to be a little creative to complete this part of the question.  For example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?

# 11.12.21 Fri
# read the bit file; 
# experimented with bits;

# 11.13.21 Sat
# convert bits into numbers; and put them into a set.

# This program is straightforward but very slow. 

import sys
import itertools
from unionFind import UnionFind

def hamDist(x, y):
    x = x ^ y
    dist = 0
 
    while x > 0:
        dist += x & 1
        x >>= 1
    return dist

def test_ham():
    p = int('11011',2)
    q = int('00101',2)
    print(hamDist(p,q))

def main():
    myset = set()
    print("read the data first!!!") 
    filename = sys.argv[1]
    with open(filename,'r') as f:
            lines = f.readlines()
            line = lines[0].split()
            print(line)
            for j in range(1,len(lines)):
                line = lines[j].split()
                # print(''.join(line))
                myset.add(int(''.join(line),2))

    L = len(myset)
    print(L)
    uf = UnionFind(L)

    mylist = list(myset)

    for pair in itertools.combinations(range(L), 2):
        # print(pair)
        p,q = pair
        if not uf.connected(p,q) and hamDist(mylist[p],mylist[q]) <=2:
            uf.union(p,q)
    print(uf.count())


if __name__ == '__main__':
    main()
