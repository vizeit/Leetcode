class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

def postorder(root):
    if root is None: return []
    stack = []
    q = [root]
    while len(q):
        n = q.pop()
        stack.append(n.val)
        for i in n.children: q.append(i)
    return stack[::-1]

if __name__ == "__main__":
    nd5 = Node(5)
    nd6 = Node(6)
    nd3 = Node(3,[nd5, nd6])
    nd2 = Node(2)
    nd4 = Node(4)
    root = Node(1, [nd3, nd2, nd4])
    print(postorder(root))