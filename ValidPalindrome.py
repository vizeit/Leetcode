from unittest import TestCase, main

class Solution:
    def isPalindrome(self, s):
        if not len(s): return True
        start, end = 0, len(s)-1
        while start < end:
            while start < end and not s[start].isalnum(): start+=1
            while start < end and not s[end].isalnum(): end-=1
            if start < end and s[start].lower()!=s[end].lower(): return False
            start, end = start+1, end-1
        return True

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            ("This is a test case", False)
        ]
    def test_isPalindrome(self):
        for p1, p2 in self.inou:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.isPalindrome(p1), p2)

if __name__ == "__main__":
    main()