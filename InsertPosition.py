def searchInsert(nums, target):
    if len(nums) == 0: return 0
    mid = len(nums) // 2
    while 1:
        if mid == len(nums) or nums[mid] == target: return mid
        elif mid < 0 or (nums[mid] < target and (mid+1 == len(nums) or nums[mid+1] > target)): return mid+1
        elif nums[mid] > target: mid -= 1
        else: mid+=1

if __name__ == "__main__":
    print(searchInsert([1,3,4], 6))
    print(searchInsert([1,3,5,6], 5))
    print(searchInsert([1,3,5,6], 2))
    print(searchInsert([1,3,5,6], 7))
    print(searchInsert([1,3,5,6], 0))
    print(searchInsert([1,3,5,6,7,8,9,10,12,13,14], 2))