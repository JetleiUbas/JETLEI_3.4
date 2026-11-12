"""
Binary Tree - UBAS

Tree (level in brackets):
        U (0)
       /     \
    B (1)    A (1)
    /
  S (2)

Expected traversals:
BFS: U - B - A - S
DFS: U - B - S - A
"""
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build(self):
        """Build the tree from the yellow-pad diagram."""
        self.root = Node("U")
        self.root.left = Node("B")
        self.root.right = Node("A")
        self.root.left.left = Node("S")

    def bfs(self):
        """Breadth-first (level order) using a queue."""
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs(self):
        """Depth-first (preorder: root, left, right) using a stack."""
        result = []
        if self.root is None:
            return result
        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


if __name__ == "__main__":
    tree = BinaryTree()
    tree.build()
    print("BFS:", " - ".join(tree.bfs()))
    print("DFS:", " - ".join(tree.dfs()))
