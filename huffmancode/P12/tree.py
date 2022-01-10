class Tree:
    def __init__(self):
        self.root = _Node(None, None)

    def maxDepth(self, node):
        if node is None:
            return -1;
        else:
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)

        if lDepth > rDepth: 
            return lDepth + 1
        else:
            return rDepth + 1

    def minDepth(self, node):
        # Corner Case.Should never be hit unless the code is
        # called on node = NULL
        if node is None:
            return -1
         
        # Base Case : Leaf node.This acoounts for height = 1
        if node.left is None and node.right is None:
            return 0
         
        # If left subtree is Null, recur for right subtree
        if node.left is None:
            return self.minDepth(node.right) + 1
         
        # If right subtree is Null , recur for left subtree
        if node.right is None:
            return self.minDepth(node.left) + 1
         
        return min(self.minDepth(node.left), self.minDepth(node.right)) + 1

class _Node:
    def __init__(self, key, val):
        self.key   = key
        self.val   = val 
        self.left  = None 
        self.right = None