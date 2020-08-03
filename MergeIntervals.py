from unittest import TestCase, main

class Solution:
    def merge(self, intervals):
        intervals.sort()
        rs = []
        for i in range(len(intervals)):
            if not rs or intervals[i][0] > rs[-1][1]:
                rs.append(intervals[i])
            else:
                if intervals[i][1] > rs[-1][1]: rs[-1][1] = intervals[i][1]
        return rs


class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
            ([[1,4],[4,5]], [[1,5]]),
            ([[0,1],[2,3],[3,5],[3,6],[3,7],[4,5],[2,3],[2,2],[7,9],[10,11],[1,1],[12,13],[2,15]], [[0,1],[2,15]])
        ]
    def test_merge(self):
        for p1, p2 in self.inou:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.merge(p1), p2)

if __name__ == "__main__":
    main()