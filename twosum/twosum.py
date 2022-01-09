import time

import sys
from instream import InStream

def readarray(file):
    instream = InStream(file)
    a = []
    while instream.hasNextLine():
        num = instream.readLine()
        a.append(int(num))
    return a

def countTarget(a, t):
    n = 0
    HT = dict()
    for x in a:
        if t-x in HT:
            return True
        HT[x] = x
    return False

def main():
    file = sys.argv[1]
    a = readarray(file)
    # a = [1,2,3,4] # test array
    N = len(a) 

    print(N)
    
    start_time = time.time()
    # print(a)
    s = set()
    for x in a:
        s.add(x)

    s = list(s)
    s.sort()
    print(len(s))
    print(s[:10])

    # temp = 0
    # M = 10
    # for t in range(-M,M+1):
    #     if countTarget(a,t) is True:
    #         temp += 1
    
    # print(temp)
    
    # end_time = time.time()
    # total_time = end_time - start_time
    # print('time:{}'.format(total_time))


if __name__ == '__main__':
    main()


# The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

# The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the i^{th} row of the file specifying the i^{th} entry of the array.

# Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)
