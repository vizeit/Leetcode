from unittest import TestCase, main

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left, right, rs = [0]*n, [0]*n, [0]*n
        left[0], right[-1] = 1, 1
        for i, j in zip(range(1,n), range(n-2, -1, -1)): left[i], right[j] = nums[i-1]*left[i-1], nums[j+1]*right[j+1]
        for i in range(n): rs[i] = left[i]*right[i]
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