class DirectedEdge:
	def __init__(self, v, w, weight):
		self._v = v
		self._w = w
		self._weight = weight

	def edge_from(self):
		return self._v 

	def edge_to(self):
		return self._w 

	def weight(self):
		return self._weight

	def __str__(self):
		s = "{}->{} {}".format(self._v, self._w, self._weight)
		return s

def main():
	e = DirectedEdge(12,34,5.67)
	print(e)

if __name__ == '__main__':
	main()