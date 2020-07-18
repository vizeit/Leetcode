class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(t1, t2):
    root = None
    if t1 and t2:
        root = TreeNode(t1.val+t2.val, mergeTrees(t1.left, t2.left), mergeTrees(t1.right, t2.right))
    elif t1:
        root = TreeNode(t1.val, mergeTrees(t1.left, None), mergeTrees(t1.right, None))
    elif t2:
        root = TreeNode(t2.val, mergeTrees(t2.left, None), mergeTrees(t2.right, None))
    return root

def printTree(t):
    if t is None:
        return
    print(t.val,end=' ')
    printTree(t.left)
    printTree(t.right)

if __name__ == "__main__":
    t5 = TreeNode(5)
    t3 = TreeNode(3, t5)
    t2 = TreeNode(2)
    t1 = TreeNode(1, t3, t2)

    t4 = TreeNode(4)
    t21 = TreeNode(1, None, t4)
    t7 = TreeNode(7)
    t23 = TreeNode(3, None, t7)
    t22 = TreeNode(2, t21, t23)
    
    t01 = TreeNode(1)
    t02 = TreeNode(2)
    print('\ntest case 1')
    printTree(mergeTrees(t01, t02))
    print('\ntest case 2')
    printTree(mergeTrees(t1, t22))

        