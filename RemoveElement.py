def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val: 
            nums.pop(i)
        else:
            i+=1
    return i+1

if __name__ == "__main__":
    l = [3,2,2,3]
    print(l[:removeElement(l, 3)])
    l = [0,1,2,2,3,0,4,2]
    print(l[:removeElement(l, 2)])