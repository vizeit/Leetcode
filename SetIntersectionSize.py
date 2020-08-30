class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda l: [l[0], -l[1]])
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            for p in range(s, s+t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                ans += 1
        return ans

if __name__ == "__main__":
    print(Solution().intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]))
    print(Solution().intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]))