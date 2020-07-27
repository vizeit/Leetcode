def searchInsert(nums, target):
    if len(nums) == 0: return 0
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target: return mid
        elif nums[mid] > target: high = mid-1
        else: low = mid+1
    return low

if __name__ == "__main__":
    print(searchInsert([1,3,4], 6))
    print(searchInsert([1,3,5,6], 5))
    print(searchInsert([1,3,5,6], 2))
    print(searchInsert([1,3,5,6], 7))
    print(searchInsert([1,3,5,6], 0))
    print(searchInsert([1,3,5,6,7,8,9,10,12,13,14], 2))