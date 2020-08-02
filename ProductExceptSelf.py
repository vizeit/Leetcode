from unittest import TestCase, main

class Solution:
    def productExceptSelf(self, nums):
        right, rs = 1, [1]*len(nums)
        for i in range(1,len(nums)): rs[i] = nums[i-1]*rs[i-1]
        for i in range(len(nums)-1, -1, -1): rs[i], right = rs[i]*right, right*nums[i]
        return rs

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inout = [
            ([1,2,3,4], [24,12,8,6]),
            ([4,5,1,8,2], [80,64,320,40,160])
        ]
    def test_productExceptSelf(self):
        for p1, p2 in self.inout:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.productExceptSelf(p1), p2)

if __name__ == "__main__":
    main()