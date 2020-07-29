from collections import defaultdict
class Counter(defaultdict):
    def __setitem__(self, key, val):
        if key in self and val == 0:
            super().pop(key)  
        else:
            if key in self and key == 0 and val > 3: val = 3
            elif key in self and key != 0 and val > 2: val = 2 
            super().__setitem__(key, val)

def threeSum(nums):
    if len(nums) < 3: return []
    rs , d = [], Counter(int)
    for i in sorted(nums,reverse=True): d[i]+=1

    while len(d):
        a = d.popitem()
        if a[0] == 0 and a[1] == 3: rs.append([0, 0, 0])
        elif a[0] >= 0: break
        if a[1] > 1: d[a[0]] = 1
        twoSum(a[0], d.copy(), rs)
        if a[1] > 1: del d[a[0]]
    return rs

def twoSum(a, nums, rs):
    target = abs(a)
    while len(nums):
        b = nums.popitem()
        if b[1] > 1: nums[b[0]] = 1
        if target-b[0] in nums:
            rs.append([a, b[0], target-b[0]])
            nums[target-b[0]] -= 1
        if b[1] > 1 and b[0] in nums: del nums[b[0]]

if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([0,0,0]))
    print(threeSum([0,4,-1,0,3,1,1,0,-3,2,-5,-4,-3,0,0,-3]))
    print(threeSum([11,2,-10,12,-10,11,9,4,2,-9,-12,-4,0,8,-6,-5,8,5,-15,-14,-1,14,-6,-12,3,-5,7,-3,9,-8,-3,-3,2,-6,-14,7,12,11,-4,-9,-13,-1,3,2,-8,12,4,7,-6,-4,1,8,-5,10,12,13,12,4,-13,-2,4,-9,10,-9,-8,4,5,-11,0,-13,-12,-6,-7,6,11,-7,-5,-8,-15,4,3,1,-11,13,-12,8,3,8,-10,5,-9,9,11,9,7,10,-2,-3,14,13]))
    
