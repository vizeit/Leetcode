def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] > nums[i]:
            nums[i+1] = nums[j]
            i += 1
    return i+1

if __name__ == "__main__":
    l = [1,1,2]
    print(l[:removeDuplicates(l)])
    l = [0,0,1,1,1,2,2,3,3,4]
    print(l[:removeDuplicates(l)])