from unittest import TestCase, main

class Solution:
    def nextPermutation(self, nums) -> None:
        end = len(nums)-1
        while end > 0:
            if nums[end-1] < nums[end]: break
            end -= 1
        if end != 0:
            send = len(nums)-1
            while send >= end:
                if nums[send] > nums[end-1]:
                    nums[send], nums[end-1] = nums[end-1], nums[send]
                    break
                send-=1
        send = len(nums)-1
        while end < send:
            nums[end], nums[send] = nums[send], nums[end]
            end += 1
            send -= 1
        

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ([2,5,4,3,1],[3,1,2,4,5]),
            ([9,8,7,6],[6,7,8,9]),
            ([1,5,8,4,7,6,5,3,1],[1,5,8,5,1,3,4,6,7]),
            ([1,5,8,4,7,1,1,1,1],[1,5,8,7,1,1,1,1,4])
        ]
    
    def test_nextPermutation(self):
        for p1, p2 in self.inou:
            with self.subTest(input=p1,expected=p2):
                l = p1
                self.solution.nextPermutation(l)
                self.assertEqual(l, p2)

if __name__ == "__main__":
    main()