from unittest import TestCase, main

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zc = 0
        while i < len(nums):
            if not nums[i]:
                zc+=1
                nums.pop(i)
            else: i+=1
        nums.extend([0]*zc)

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