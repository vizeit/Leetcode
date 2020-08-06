from unittest import TestCase, main

class Solution:
    def isAlienSorted(self, words, order):
        order_index = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]: return False
                    break
            else:
                if len(word1) > len(word2): return False
        return True

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
            (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False),
            (["apple","app"], "abcdefghijklmnopqrstuvwxyz", False)
        ]
    def testisAlienSorted(self):
        for p1, p2, p3 in self.inou:
            with self.subTest(words=p1, order=p2, expected=p3):
                self.assertEqual(self.solution.isAlienSorted(p1, p2),p3)

if __name__ == "__main__":
    main()