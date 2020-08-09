from unittest import TestCase, main

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root, target):
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_closestValue(self):
        n1, n3, n5 = TreeNode(1), TreeNode(3), TreeNode(5)
        n2 = TreeNode(2, n1, n3)
        n4 = TreeNode(4, n2, n5)
        self.assertEqual(self.solution.closestValue(n4, 3.714286), 4)
        self.assertEqual(self.solution.closestValue(n4, 1.714286), 2)

if __name__ == "__main__":
    main()