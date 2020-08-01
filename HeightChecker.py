import unittest

def heightChecker(heights):
    return sum(1 for i,j in zip(heights,sorted(heights)) if i != j)


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