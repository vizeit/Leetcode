def maxProduct(nums):
    nums = sorted(nums)[-2:] if len(nums) > 2 else nums
    return (nums[0]-1)*(nums[1]-1)

if __name__ == "__main__":
    print(maxProduct([3,4,5,2]))
    print(maxProduct([1,5,4,5]))
    print(maxProduct([3,7]))