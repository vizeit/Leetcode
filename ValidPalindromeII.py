from unittest import TestCase, main

class Solution:
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        for i in range(len(s)-1):
            if s[i] != s[-i-1]:
                return s[i: -i-2] == s[i+1: -i-1][::-1] or s[i+1: -i-1] == s[i+2: len(s)-i][::-1]
        return False

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