class Solution:
    def shortestDistance(self, words, word1, word2) -> int:
        i1, i2, mindist = -1, -1, len(words)
        for i, w in enumerate(words):
            if w == word1: i1 = i
            elif w == word2: i2 = i
            if i1 != -1 and i2 != -1:
                mindist = min(mindist, abs(i1-i2))
        return mindist

if __name__ == "__main__":
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "makes"))
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "perfect"))
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "practice", "makes"))
    