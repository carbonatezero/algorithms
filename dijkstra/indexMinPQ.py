from deprecated import deprecated
import stdio

class IndexMinPQ:
    def __init__(self, maxN):
        self._maxN = maxN  # maximum number of elements on PQ
        self._n = 0        # number of elements on PQ
        self._pq = dict()  # binary heap using 1-based indexing
        self._qp = dict()  # inverse of pq : qp[pq[i]] = pq[qp[i]] = i
        self._keys = dict()    # keys[i] = priority of i
        for i in range(maxN+1):
            self._qp[str(i)] = -1

    def isEmpty(self): 
        return self._n == 0   
    
    def contains(self, i): 
        return self._qp[i] != -1

    def size(self): 
        return self._n

    def insert(self, i, key): 
        if self.contains(i): 
            raise ValueError("index is already in the priority queue")
        self._n += 1
        self._qp[i] = self._n
        self._pq[self._n] = i
        self._keys[i] = key
        self._swim(self._n)

    def changeKey(self, i, key): 
        if not self.contains(i):
            raise ValueError("index is not in the priority queue")
        self._keys[i] = key 
        self._swim(self._qp[i])
        self._sink(self._qp[i])

    @deprecated
    def change(self, i, key):
        self.changeKey(i,key) 
    
    def delMin(self): 
        if self._n == 0:
            raise ValueError("Priority queue underflow")
        mini = self._pq[1]
        self._exch(1, self._n)
        self._n -= 1
        self._sink(1)
        assert mini == self._pq[self._n+1]
        self._qp[mini] = -1 
        self._keys[mini] = None 
        self._pq[self._n+1] = -1 
        return mini
     
    
    # def delete(self, k): pass 
    # def min(self): pass 
    # def minIndex(self): pass 
     

    # ------------------------------------------------------------------
    # Helper functions.
    # ------------------------------------------------------------------
    def _greater(self, i, j):
        # return keys[pq[i]].compareTo(keys[pq[j]]) > 0
        return self._keys[self._pq[i]] > self._keys[self._pq[j]]

    def _exch(self, i, j):
        swap = self._pq[i]
        self._pq[i] = self._pq[j]
        self._pq[j] = swap
        self._qp[self._pq[i]] = i
        self._qp[self._pq[j]] = j 

    def _swim(self, k): 
        while k > 1 and self._greater(k//2, k):
            self._exch(k, k//2)
            k = k // 2

    def _sink(self, k): 
        while 2*k <= self._n:
             j = 2*k 
             if j < self._n and self._greater(j, j+1): j += 1
             if not self._greater(k,j): break
             self._exch(k,j)
             k = j

def main():
    # insert a bunch of strings
    strings = ["it", "was", "the", "best", "of", "times", "it", "was", "the", "worst"] 
    strings = [7.1, 4.4, 3, 44, 5, 8, 9, 11]
    # strings = ["G", "S", "R", "P", "N", "O", "A", "E", "I", "T", "H"]
    for i in range(len(strings)):
        print("{:2d}: {}".format(i,strings[i]))

    print(30*"*")
    pq = IndexMinPQ(len(strings))
    for i in range(len(strings)):
        pq.insert(i, strings[i])
    
    # delete and print each key
    while pq.isEmpty() is not True:
        i = pq.delMin()
        print("{:2d}: {}".format(i,strings[i]))


if __name__ == '__main__':
    main()
     