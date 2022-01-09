# https://www.youtube.com/watch?v=VmogG01IjYc
# https://www.hackerrank.com/challenges/find-the-running-median/problem

from maxPQ import MaxPQ
from minPQ import MinPQ

import sys
from instream import InStream

class RunningMedian:
    def __init__(self, a):
        N = len(a)
        self._low  = MaxPQ(N//2+1)
        self._high = MinPQ(N//2+1)

        self._medians = [0 for _ in range(N)]
        
        for i in range(N):
            number = a[i]
            self._addNumber(number)
            self._rebalance()
            self._medians[i] = self._getMedian(self._low, self._high)


    def _addNumber(self, number):
        if (self._low.isEmpty() or number < self._low.root()):
            self._low.insert(number)
        else:
            self._high.insert(number)

    def _rebalance(self):
        if self._low.size() > self._high.size() + 1 : 
            self._high.insert(self._low.delRoot())
        elif self._high.size() > self._low.size() + 1 :
            self._low.insert(self._high.delRoot())

    def _getMedian(self, low, high):
        if low.size() > high.size(): 
            biggerHeap  = low
            smallerHeap = high
        else:
            biggerHeap  = high
            smallerHeap = low

        if (biggerHeap.size() - smallerHeap.size() == 0):
            return smallerHeap.root()
        else:
            return biggerHeap.root()

    def medians(self):
        return self._medians
    

def readarray(file):
    instream = InStream(file)
    a = []
    while instream.hasNextLine():
        num = instream.readLine()
        a.append(int(num))
    return a

def main():
    file = sys.argv[1]
    a = readarray(file)
    # a = [7.1, 4.4, 3, 44, 5, 8, 9, 11] # test array
    N = len(a)

    solution = RunningMedian(a)
    medians = solution.medians()
    print((sum(medians))%10000)
    


if __name__ == '__main__':
    main()