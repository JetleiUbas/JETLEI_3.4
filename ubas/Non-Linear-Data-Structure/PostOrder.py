
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=" ")


# Binary Tree: JETLEI UBAS
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


print("FULL NAME: JETLEI UBAS")
print("POSTORDER TRAVERSAL:")
post_order(root)
