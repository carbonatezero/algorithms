# https://github.com/tiefenauer/stanford-algorithms/blob/master/03-greedy-alorithms-minimum-spanning-trees-dynamic-programming/week-02/clustering_big.py

import itertools
import sys
from unionFind import UnionFind

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        lines = f.readlines()

    n_nodes, n_bits = map(int, lines[0].split())
    print(f'{n_nodes} nodes')
    print(f'{n_bits} bits per node')

    numbers = [int(''.join(line.split()), 2) for line in lines[1:]]
    nodes = {} # initialize a dictionary
    for node, num in enumerate(numbers):
        if num not in nodes:
            nodes[num] = set()
        nodes[num].add(node)

    

    # translate bit differences into integer differences:
    distances = [1 << i for i in range(n_bits)]
    print(distances)
    print(40*'-')
    distances += [(1 << ix_1) ^ (1 << ix_2) 
                   for (ix_1, ix_2) in itertools.combinations(range(n_bits), 2)]
    distances.append(0)

    print(distances)
    print(40*'-')

    print(n_nodes)
    print(len(nodes.keys())) # 198788
    print(len(distances))

    
    # # uf = UnionFind(range(n_nodes))
    uf = UnionFind(n_nodes)

    for distance in distances:
        for number in nodes.keys():
            if (number ^ distance) in nodes:
                for node_from in nodes[number]:
                    for node_to in nodes[number ^ distance]:
                        uf.union(node_from, node_to)
    # print(len(list(uf.to_sets())))  # 6118
    print(uf.count())
