
# ASSESSMENT 3.5
# PREORDER TRAVERSAL
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


# PreOrder Function
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Display Output
print("FULL NAME: JETLEI UBAS")
print("ASSESSMENT 3.5 - PREORDER")
print("Root -> Left -> Right")

print("\nPreOrder Traversal:")
preorder(root)
