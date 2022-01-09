from deprecated import deprecated
import stdio

class MinPQ:
    def __init__(self, maxN):
        self._maxN = maxN  # maximum number of elements on PQ
        self._n = 0        # number of elements on PQ
        self._pq = dict()  # binary heap using 1-based indexing

    def isEmpty(self):
        '''
        Returns true if this priority queue is empty.

        ''' 
        return self._n == 0

    def size(self):
        '''
        Returns the number of keys on this priority queue.

        ''' 
        return self._n

    def root(self):
        '''
        Returns a largest key on this priority queue.

        '''
        if (self.isEmpty()): raise ValueError("Priority queue underflow")
        return self._pq[1] 

    def insert(self, x): 
        self._n += 1
        self._pq[self._n] = x 
        self._swim(self._n)
    
    def delRoot(self): 
        if (self.isEmpty()): raise ValueError("Priority queue underflow")
        maxi = self._pq[1]
        self._exch(1, self._n)
        self._n -= 1
        self._sink(1)
        self._pq[self._n+1] = None
        return maxi

    # ------------------------------------------------------------------
    # Helper functions to restore the heap invariant.
    # ------------------------------------------------------------------
    def _swim(self, k): 
        while k > 1 and self._less(k//2, k):
            self._exch(k, k//2)
            k = k // 2

    def _sink(self, k): 
        while 2*k <= self._n:
             j = 2*k 
             if j < self._n and self._less(j, j+1): j += 1
             if not self._less(k,j): break
             self._exch(k,j)
             k = j

    # ------------------------------------------------------------------
    # Helper functions for compares and swaps.
    # ------------------------------------------------------------------
    def _less(self, i, j):
        return self._pq[i] > self._pq[j]

    def _exch(self, i, j):
        swap = self._pq[i]
        self._pq[i] = self._pq[j]
        self._pq[j] = swap
    
    

def main():
    # insert a bunch of strings
    strings = ["it", "was", "the", "best", "of", "times", "it", "was", "the", "worst"] 
    strings = [7.1, 4.4, 3, 44, 5, 8, 9, 11]
    # strings = ["G", "S", "R", "P", "N", "O", "A", "E", "I", "T", "H"]
    for i in range(len(strings)):
        print("{:2d}: {}".format(i,strings[i]))

    print(30*"*")
    pq = MinPQ(len(strings))
    for i in range(len(strings)):
        pq.insert(strings[i])
        print(pq.root())
    
    print(30*"*")
    # delete and print each key
    while pq.isEmpty() is not True:
        x = pq.delRoot()
        print("{}".format(x))


if __name__ == '__main__':
    main()
     