from unittest import TestCase, main

class Solution:
    def maxProfit(self, prices):
        minprice, maxprofit = float('inf'), 0
        for i in range(len(prices)):
            if prices[i] < minprice: minprice = prices[i]
            elif prices[i] - minprice > maxprofit: maxprofit = prices[i]-minprice
        return maxprofit

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ([7,1,5,3,6,4], 5),
            ([7,6,4,3,1], 0)
        ]
    
    def test_maxProfit(self):
        for p1, p2 in self.inou:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.maxProfit(p1),p2)

if __name__ == "__main__":
    main()