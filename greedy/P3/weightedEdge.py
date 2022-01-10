class WeightedEdge:
    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def either(self):
        return self._v 

    def other(self,vertex):
        if vertex == self._v:
            return self._w 
        elif vertex ==self._w:
            return self._v 

    def weight(self):
        return self._weight

    def __lt__(self, obj):
        """self < obj."""
        return self.weight() < obj.weight()

    def __str__(self):
        s = "{}-{} {}".format(self._v, self._w, self._weight)
        return s

def main():
    e = WeightedEdge(12,34,5.67)
    print(e)

if __name__ == '__main__':
    main()