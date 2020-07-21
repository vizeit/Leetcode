class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

def preorder(root):
    if root is None: return []
    result = []
    stack = [root]
    while len(stack):
        n = stack.pop()
        result.append(n.val)
        for i in range(len(n.children)-1,-1,-1): stack.append(n.children[i])
    return result

if __name__ == "__main__":
    nd5 = Node(5)
    nd6 = Node(6)
    nd3 = Node(3,[nd5, nd6])
    nd2 = Node(2)
    nd4 = Node(4)
    root = Node(1, [nd3, nd2, nd4])
    print(preorder(root))