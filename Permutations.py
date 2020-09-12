class Solution:
    def permute(self, nums):
        def backtrack(first = 0):
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

if __name__ == "__main__":
    print(Solution().permute([1,2,3]))
    print(Solution().permute(['a','b','c']))