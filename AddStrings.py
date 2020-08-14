from unittest import TestCase, main
from itertools import zip_longest
class Solution:
    def AddStrings(self, num1, num2):
        c, s = 0, []
        for i, j in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            t = c + (ord(i)-48) + (ord(j)-48)
            c, t = divmod(t,10)
            s.append(chr(t+48))
        if c: s.append('1')
        return ''.join(s[::-1])

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ('','',''),
            ('12','21','33'),
            ('12','21','33'),
            ('2378274982379472','3987498739','2378278969878211'),
            ('99999999999999999999','99999999999999999999','199999999999999999998'),
            ('23782749823794722837428947328974892374983274893279847328947328974892323428048209','39874987398349284039284092840923840982304802938409328094820984028409284098230877', '63657737222144006876713040169898733357288077831689175423768313003301607526279086')
        ]

    def test_AddStrings(self):
        for p1, p2, p3 in self.inou:
            with self.subTest(num1=p1,num2=p2,expected=p3):
                self.assertEqual(self.solution.AddStrings(p1,p2),p3)


if __name__ == "__main__":
    main()