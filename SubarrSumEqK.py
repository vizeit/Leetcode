from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        d = defaultdict(int)
        d[0] = 1
        su = 0
        c = 0
        for n in nums:
            su+=n
            if su-k in d: c+=d[su-k]
            d[su]+=1
        return c

if __name__ == "__main__":
    print(Solution().subarraySum([3,4,7,2,-3,1,4,2], 7))
    print(Solution().subarraySum([1,0,1,2,-1], 2))