# This file describes an instance of the problem. It has the following format:

# [number_of_symbols]

# [weight of symbol #1]

# [weight of symbol #2]

# ...

# For example, the third line of the file is "6852892," indicating that the weight of the second symbol of the alphabet is 6852892.  (We're using weights instead of frequencies, like in the "A More Complex Example" video.)

# Your task in this problem is to run the Huffman coding algorithm from lecture on this data set. 

# Questions
# What is the maximum length of a codeword in the resulting Huffman code?
# What is the minimum length of a codeword in your Huffman code?

# 11.16.21 Tue
# Next step: read princeton algo4 ch5.5

# 11.17.21 Wed
# Read algo4; not very useful for this assignment;
# Tried to read the textbook; Focused on a smaller problem;
# Next step: think about the straightforward implementation of the "main loop"

# 11.18.21 Thu
# Need min/max depth of a tree
# Next step: work on the binary tree!
# worked out a version that JUST answers the questions

import sys
from tree import Tree

def mergeTree(T1,T2):
    T3 = Tree()
    T3.root.left  = T1.root 
    T3.root.right = T2.root
    return T3

def huffman(freq):
    # Initialization
    F = {}
    for a in range(1,len(freq)):
        T = Tree()
        F[T] = freq[a]

    # Main loop
    while len(F) > 1:
        F_sorted = sorted(F.items(), key=lambda x: x[1])
        T1, pT1 = F_sorted[0][0], F_sorted[0][1]
        T2, pT2 = F_sorted[1][0], F_sorted[1][1]
        del F[T1]
        del F[T2]
        T3 = mergeTree(T1,T2)
        pT3 = pT1 + pT2
        F[T3] = pT3
    return list(F.keys())[0]

def readFreq(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        for j in range(len(lines)):
            lines[j] = int(lines[j].strip())
    # print(lines[:5])
    return lines


def main():
    print('greedy huffman.')
    print('read data from file first.')
    filename = sys.argv[1]
    freq = readFreq(filename)
    print(freq[:5])

    F = huffman(freq)
    # print(F)
    mindepth = F.minDepth(F.root)
    maxdepth = F.maxDepth(F.root)

    print(mindepth)
    print(maxdepth)

    
    

if __name__ == '__main__':
	main()