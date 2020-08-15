from unittest import TestCase, main
from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, words, k):
        h = [(-c, key) for key, c in Counter(words).items()]
        heapify(h)
        return [heappop(h)[1] for _ in range(k)]

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            (["i", "love", "leetcode", "i", "love", "coding"],2,["i", "love"]),
            (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4,["the", "is", "sunny", "day"])
        ]
    def test_topKFrequent(self):
        for p1, p2, p3 in self.inou:
            with self.subTest(inputarr=p1,outvalues=p2,expected=p3):
                self.assertEqual(self.solution.topKFrequent(p1, p2),p3)

if __name__ == "__main__":
    main()