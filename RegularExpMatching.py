from unittest import TestCase, main

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

class testsolution(TestCase):
    def setUp(self):
        self.Solution = Solution()
        self.io = [
            ("aa","a", False),
            ("aa","a*", True),
            ("ab",".*", True),
            ("aab","c*a*b", True),
            ("mississippi","mis*is*p*.", False)
        ]
        
    def test_isMatch(self):
        for p1, p2, p3 in self.io:
            with self.subTest(inputstr=p1, pattern=p2, ismatch=p3):
                self.assertEqual(self.Solution.isMatch(p1, p2), p3)

if __name__ == "__main__":
    main()