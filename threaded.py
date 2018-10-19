class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.threaded = False

def populateQueue(root, q):
    if root is None:
        return
    
    if root.left is not None:
        populateQueue(root.left, q)
    q.append(root)

    if root.right is not None:
        populateQueue(root.right, q)

def createThreaded_util(root, queue):
    if root is None:
        return

    if root.left is not None:
        createThreaded_util(root.left, queue)

    queue.pop(0)

    if root.right is not None:
        createThreaded_util(root.right, queue)
    elif queue:
        root.right = queue[0]
        root.threaded = True


def leftMost(node):
    while node is not None and node.left is not None:
        node = node.left
    return node


def inOrder(node):
    if node is None:
        return

    cur = leftMost(node)
    while cur is not None:
        print(cur.key, end=' ')
        if cur.threaded:
            cur = cur.right
        else:
            cur = leftMost(cur.right)
    print("\n")

def createThreaded(root):
    queue = []
    populateQueue(root, queue)
    createThreaded_util(root, queue)

if __name__ == '__main__':
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.left = Node('F')
    root.right.right = Node('G')
    root.left.left.left = Node('H')
    root.left.left.right = Node('I')
    root.right.left.right = Node('J')

    createThreaded(root)
    print("---------------")
    inOrder(root)
