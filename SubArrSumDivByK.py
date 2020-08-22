from itertools import accumulate
from collections import Counter
class Solution(object):
    def subarraysDivByK(self, A, K):
        return sum(v*(v-1)//2 for v in Counter(accumulate(A, lambda x,y: (x+y)%K, initial=0)).values())

if __name__ == "__main__":
    print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))