# improved the solution in:
# https://github.com/tiefenauer/stanford-algorithms/blob/master/03-greedy-alorithms-minimum-spanning-trees-dynamic-programming/week-02/clustering_big.py

import itertools
import sys
from unionFind import UnionFind

def main():
    numbers = set()
    print("read the data from file first.") 
    filename = sys.argv[1]
    with open(filename,'r') as f:
            lines = f.readlines()
            n_nodes, n_bits = map(int, lines[0].split())
            print(f'{n_nodes} nodes')
            print(f'{n_bits} bits per node')
            for j in range(1,len(lines)):
                line = lines[j].split()
                numbers.add(int(''.join(line),2))
   
    numbers = list(numbers)
 
    nodes = {}
    for node, num in enumerate(numbers):
        nodes[num] = node
    
    # translate bit differences into integer differences:
    distances = [1 << i for i in range(n_bits)]
    distances += [(1 << ix_1) ^ (1 << ix_2) 
                   for (ix_1, ix_2) in itertools.combinations(range(n_bits), 2)]

    L  = len(numbers)
    uf = UnionFind(L)

    for distance in distances:
        for number in nodes.keys():
            q = number ^ distance
            if q in nodes:
                uf.union(nodes[number],nodes[q])
    print(uf.count()) # 6118

if __name__ == "__main__":
    main()
