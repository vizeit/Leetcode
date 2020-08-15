from unittest import TestCase, main
from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        d = Counter(words)
        d = sorted(Counter(words), key=lambda x:(-d[x], x))
        return d[:k]

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