def threeSum(nums):
    if len(nums) < 3: return []
    nums.sort()
    rs = []
    for i in range(len(nums)):
        if nums[i] > 0: break
        if i > 0 and nums[i] == nums[i-1]: continue
        twoSum(i, nums, rs)
    return rs

def twoSum(i, nums, rs):
    d, target = {}, abs(nums[i])
    for j in range(len(nums)-1, i, -1):
        if nums[j] != 0 and j > 1 and nums[j] == nums[j-1] and nums[j-1] == nums[j-2]: continue
        elif j > 2 and nums[j] == 0 and nums[j] == nums[j-1] and nums[j-1] == nums[j-2] and nums[j-2] == nums[j-3]: continue
        if nums[j] in d: 
            rs.append([nums[i], nums[j], nums[d[nums[j]]]])
            del d[nums[j]]
        else: 
            d[target-nums[j]] = j

if __name__ == "__main__":
    print(threeSum([0,0,0]))
    print(threeSum([0,4,-1,0,3,1,1,0,-3,2,-5,-4,-3,0,0,-3]))
    print(threeSum([11,2,-10,12,-10,11,9,4,2,-9,-12,-4,0,8,-6,-5,8,5,-15,-14,-1,14,-6,-12,3,-5,7,-3,9,-8,-3,-3,2,-6,-14,7,12,11,-4,-9,-13,-1,3,2,-8,12,4,7,-6,-4,1,8,-5,10,12,13,12,4,-13,-2,4,-9,10,-9,-8,4,5,-11,0,-13,-12,-6,-7,6,11,-7,-5,-8,-15,4,3,1,-11,13,-12,8,3,8,-10,5,-9,9,11,9,7,10,-2,-3,14,13]))
    
