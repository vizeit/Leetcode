from unittest import TestCase, main

class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in range(n-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.io = [
            (1, 10),
            (2, 20),
            (3, 46),
            (4, 104),
            (3131, 136006598)
        ]
    
    def test_knightDialer(self):
        for p1, p2 in self.io:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.knightDialer(p1), p2)

if __name__ == "__main__":
    main()