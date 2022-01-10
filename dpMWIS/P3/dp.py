# This file describes the weights of the vertices in a path graph (with the weights listed in the order in which vertices appear in the path). It has the following format:

# [number_of_vertices]

# [weight of first vertex]

# [weight of second vertex]

# ...

# For example, the third line of the file is "6395702," indicating that the weight of the second vertex of the graph is 6395702. 

# Your task in this problem is to run the dynamic programming algorithm (and the reconstruction procedure) from lecture on this data set.  

# The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong to the maximum-weight independent set?  

# (By "vertex 1" we mean the first vertex of the graph---there is no vertex 0.)   In the box below, enter a 8-bit string, where the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight independent set, and 0 otherwise. For example, if you think that the vertices 1, 4, 17, and 517 are in the maximum-weight independent set and the other four vertices are not, then you should enter the string 10011010 in the box below.

# 11.19.21 Fri. 
# Done in one day

import sys 

def getmwis(w):
    # w[0] = num. of vertices;
    # w[1],...,w[n]: weights of n vertices
    n = len(w) - 1
    A = [0 for _i in range(n+1)]
    A[0] = 0
    A[1] = w[1]
    for i in range(2,n):
        A[i] = max(A[i-1], A[i-2]+w[i])

    # reconstruction
    S = set()
    i = n
    while i >= 1:
        if A[i-1] >= A[i-2]+w[i]:
            i -= 1 
        else:
            S.add(i)
            i -= 2
    return A, S

def readWeights(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        for j in range(len(lines)):
            lines[j] = int(lines[j].strip())
    return lines

def main():
    # read data
    filename = sys.argv[1]
    weights  = readWeights(filename)
    print(weights[:5])

    A, S = getmwis(weights)

    soln = []
    question_List = [1, 2, 3, 4, 17, 117, 517, 997]
    # get the output 
    for e in question_List:
        if e in S:
            soln.append('1')
        else:
            soln.append('0')
    print(''.join(soln))


if __name__ == '__main__':
    main()