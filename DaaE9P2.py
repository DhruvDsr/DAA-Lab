class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = self.right = None

def count_nodes(root):
    def get_height(node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    if not root:
        return 0
    left_h = get_height(root.left)
    right_h = get_height(root.right)
    
    if left_h == right_h:
        return (1 << left_h) + count_nodes(root.right)
    else:
        return (1 << right_h) + count_nodes(root.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
print(count_nodes(root))