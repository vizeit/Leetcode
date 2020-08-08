from unittest import TestCase, main

class Solution:
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            (["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"], ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]),
            (["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"], ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])
        ]
    
    def test_reorderLogFiles(self):
        for p1, p2 in self.inou:
            with self.subTest(input=p1, expected=p2):
                self.assertEqual(self.solution.reorderLogFiles(p1), p2)

if __name__ == "__main__":
    main()