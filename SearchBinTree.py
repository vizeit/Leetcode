# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def printtree(self, root):
        if root == None:
            return
        print(root.val)
        self.printtree(root.left)
        self.printtree(root.right)

def searchBST(root: TreeNode, val: int) -> TreeNode:
    if root == None or root.val == val:
        return root
    elif val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)

if __name__ == "__main__":
    t1 = TreeNode(1)
    t3 = TreeNode(3)
    t2 = TreeNode(2, t1, t3)
    t7 = TreeNode(7)
    root = TreeNode(4, t2, t7)
    TreeNode().printtree(searchBST(root, 2))
