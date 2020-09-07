from unittest import TestCase, main
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums):
        return sum(v*(v-1)//2 for v in Counter(nums).values())

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.io = [
            ([1,2,3,1,1,3], 4),
            ([1,1,1,1], 6),
            ([1,2,3], 0),
            ([2,2,2], 3)
        ]

    def test_numIdenticalPairs(self):
        for p1, p2 in self.io:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.numIdenticalPairs(p1), p2)
    
if __name__ == "__main__":
    main()