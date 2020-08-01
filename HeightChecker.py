import unittest

def heightChecker(heights):
    A = [0]*101
    c, p = 0, 1
    for i in heights: A[i]+=1
    for j in heights:
        while A[p] == 0: p+=1
        if p != j: c+=1
        A[p]-=1
    return c


class testsolution(unittest.TestCase):
    def setUp(self):
        self.input_output = [
            ([1,1,4,2,1,3], 3),
            ([5,1,2,3,4], 5),
            ([1,2,3,4,5], 0)
            ]
        
    def test_heightChecker(self):
        for p1, p2 in self.input_output:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(heightChecker(p1),p2)
                self.assertEqual(heightChecker(p1),p2)
                self.assertEqual(heightChecker(p1),p2)

if __name__ == "__main__":
    unittest.main()