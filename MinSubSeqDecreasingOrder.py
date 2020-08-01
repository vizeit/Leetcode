from unittest import TestCase, main
from heapq import heappush, heappop

class solution:
    def minSubsequence(self, nums):
        l = []
        s = 0
        for i in nums:
            heappush(l, -i)
            s+=i
        nums.clear()
        ss = 0
        while len(l):
            t = -heappop(l)
            s -= t
            ss += t
            nums.append(t)
            if ss > s: break
        return nums

class testsolution(TestCase):
    def setUp(self):
        self.solution = solution()
        self.input_output = [
            ([4,3,10,9,8], [10,9]),
            ([4,4,7,6,7], [7,7,6]),
            ([6], [6])
        ]
    def test_minSubsequence(self):
        for p1, p2 in self.input_output:
            with self.subTest(input=p1, expectedoutput=p2):
                self.assertEqual(self.solution.minSubsequence(p1),p2)

if __name__ == "__main__":
    main()