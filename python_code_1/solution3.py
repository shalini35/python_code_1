from queue import Queue

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

def breadth_first_traversal(root):
    
    if root==None:
        return -1
    
    q = Queue(maxsize = 500)
    q.put(root)

    level_order_traversal = []
    while(not q.empty()):
        
        node = q.get()
        level_order_traversal.append(str(node.data))

        if node.left != None:
            q.put(node.left)
        if node.right != None:
            q.put(node.right)
        
    return level_order_traversal

root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
    
path = "->".join(breadth_first_traversal(root))
print("level order traversal: ",path)