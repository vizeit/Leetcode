from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, A, K):
        d = defaultdict(int)
        d[0] = 1
        su = 0
        for x in A:
            su += x
            d[su % K]+=1

        return sum(v*(v-1)//2 for v in d.values())

if __name__ == "__main__":
    print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 2))