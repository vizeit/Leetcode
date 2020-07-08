class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def rangeSumBST(root, l, r):
    rs = [0]
    _subrangeSumBST(root, l, r, rs)
    return rs[0]

def _subrangeSumBST(root, l, r, s):
    if root == None:
        return
    _subrangeSumBST(root.left, l, r, s)
    if root.val >= l and root.val <= r:
        s[0]+=root.val
    if root.val >= r:
        return
    _subrangeSumBST(root.right, l, r, s)
if __name__ == "__main__":
    h1 = TreeNode(3)
    h2 = TreeNode(7)
    h3 = TreeNode(5, h1, h2)
    h4 = TreeNode(18)
    h5 = TreeNode(15,None,h4)
    h = TreeNode(10, h3, h5)
    print(rangeSumBST(h, 7, 15))