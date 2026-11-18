
# ASSESSMENT 3.5
# INORDER TRAVERSAL
# FULL NAME: JETLEI UBAS

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("J")

root.left = Node("E")
root.right = Node("T")

root.left.left = Node("L")
root.left.right = Node("E")

root.right.left = Node("I")
root.right.right = Node("U")

root.left.left.left = Node("B")
root.left.left.right = Node("A")

root.left.right.left = Node("S")


# InOrder Function
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Display Output
print("FULL NAME: JETLEI UBAS")
print("ASSESSMENT 3.5 - INORDER")
print("Left -> Root -> Right")

print("\nInOrder Traversal:")
inorder(root)
