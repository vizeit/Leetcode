from unittest import TestCase, main

class Solution:
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ("deeee", True),
            ("tcaac", True),
            ("aba", True),
            ("abca", True),
            ("itopinonavzyevanonipoti", False),
            ("itopinonavzevanonipoti", True),
            ("itopinonavevanonipoti", True)
        ]
    def test_validPalindrome(self):
        for p1, p2 in self.inou:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.validPalindrome(p1),p2)

if __name__ == "__main__":
    main()