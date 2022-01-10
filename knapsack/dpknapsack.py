# In this programming problem and the next you'll code up the knapsack algorithm from lecture.

# Let's start with a warm-up.  Download the text file below.

# This file describes a knapsack instance, and it has the following format:

# [knapsack_size][number_of_items]

# [value_1] [weight_1]

# [value_2] [weight_2]

# ...

# For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.

# You can assume that all numbers are positive.  You should assume that item weights and the knapsack capacity are integers.

# In the box below, type in the value of the optimal solution.

# ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

# -----------------------------------------------------------------------------------

# This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space.  So you will have to be creative to compute an optimal solution.  

# One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis.  Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.

# 11.21.21 Sun
# Warming-up problem is easy. Done.
# Next step: revisit the lecture again to see possibility of improvement

# 11.22.21 Mon
# identified redundant work in the main loops

import sys
import numpy as np
import threading

def readData(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        v = []
        w = []
        for j in range(len(lines)):
            a,b = lines[j].split()
            v.append(int(a))
            w.append(int(b))
    return v, w

def dpKnapsack(v,w):
    n = w[0]
    W = v[0]
    # print(W,n)

    A = [[0 for _x in range(W+1)] for _i in range(n+1)]

    for i in range(1,n+1):
        for x in range(W+1):
            if x < w[i]:
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x], A[i-1][x-w[i]]+v[i])
    # print(A)
    # print(40*'-')
    return A[n][W]

def dpKnapsack_big(v,w):
    '''
    slight improvement: use only two columns of A

    '''
    n = w[0]
    W = v[0]
    # print(W,n)

    A = [[0 for _x in range(W+1)],[0 for _x in range(W+1)]]
    for k in range(1,n+1):
        i = k % 2
        for x in range(w[k]):
            A[i][x] = A[i-1][x]
        for x in range(w[k],W+1):
            A[i][x] = max(A[i-1][x], A[i-1][x-w[k]]+v[k])
        # A[i-1] = []
    # print(A)
    # print(40*'-')
    return A[n%2][W]

def dpKnapsack_np(v,w):
    '''
    slight improvement: use only two columns of A;
    and try numpy array

    '''
    n = w[0]
    W = v[0]
    # print(W,n)

    A = np.array([[0 for _x in range(W+1)],[0 for _x in range(W+1)]])
    for k in range(1,n+1):
        i = k % 2
        for x in range(w[k]):
            A[i][x] = A[i-1][x]
        for x in range(w[k],W+1):
            A[i][x] = max(A[i-1][x], A[i-1][x-w[k]]+v[k])
    # print(A)
    # print(40*'-')
    return A[n%2][W]

def dpKnapsack_recursive(i,x):
    A = dict()
    def getA(i,x):
        str_ix = str(i) + ":" + str(x)
        if str_ix in A:
            return A[str_ix]
        if i == 0:
            return 0
        else:
            if x < w[i]:
                A[str_ix] = getA(i-1,x)
            else:
                A[str_ix] = max(getA(i-1,x), getA(i-1,x-w[i])+v[i])
        return A[str_ix]
    return getA(i,x)


def main():
    print("dpkapsack.py")
    file = sys.argv[1]
    global v, w
    v, w = readData(file) 
    print(v[0],w[0])

    soln = 0
    # soln = dpKnapsack(v,w) # 2493893
    # soln = dpKnapsack_big(v,w)
    # soln = dpKnapsack_np(v,w)

    n,W = w[0],v[0]
    soln = dpKnapsack_recursive(n,W) # 4243395
    print(soln)


if __name__ == '__main__':
    threading.stack_size(64 * 1024 * 1024)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target=main)
    thread.start()