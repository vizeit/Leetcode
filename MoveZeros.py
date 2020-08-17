from unittest import TestCase, main
"""
approach 1: remove zeros, append them at the end. better performance than approach 2
approach 2: swap items at respective position
"""
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        lastnonzero = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[lastnonzero], nums[i] = nums[i], nums[lastnonzero]
                lastnonzero +=1

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.io = [
            ([0,1,0,3,12], [1,3,12,0,0]),
            ([0,0,0,0,0,1], [1,0,0,0,0,0])
        ]
    def test_moveZeroes(self):
        for p1, p2 in self.io:
            with self.subTest(input=p1, expected=p2):
                self.solution.moveZeroes(p1)
                self.assertEqual(p1, p2)

if __name__ == "__main__":
    main()