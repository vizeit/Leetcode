def searchInsert(nums, target):
    if len(nums) == 0: return 0
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return i+1

if __name__ == "__main__":
    print(searchInsert([1,3,5,6], 5))