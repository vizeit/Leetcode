from unittest import TestCase, main

class Solution:
    def searchRange(self, nums, target):
        left = self.findtargetindex(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        return [left, self.findtargetindex(nums, target, False)-1]
        
    def findtargetindex(self, nums, target, left=True):
        start, end = 0, len(nums)
        while start < end:
            mid = (start+end) // 2
            if nums[mid] > target or (left and nums[mid]==target):
                end = mid
            else:
                start = mid+1
        return start

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ([5,7,7,8,8,10], 8, [3,4]),
            ([5,7,7,8,8,10], 6, [-1,-1]),
            ([5,7,7,8,9,10], 8, [3,3]),
            ([5,5,7,8,9,10], 5, [0,1]),
            ([5,7,7,8,10,10], 10, [4,5])
        ]
    def test_searchRange(self):
        for p1,p2,p3 in self.inou:
            with self.subTest(input=p1, target=p2, expected=p3):
                self.assertEqual(self.solution.searchRange(p1,p2),p3)

if __name__ == "__main__":
    main()