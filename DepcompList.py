def decompressRLElist(nums):
    return [nums[j] for i,j in zip(range(0, len(nums), 2), range(1, len(nums),2)) for k in range(nums[i])]

if __name__ == "__main__":
    print(decompressRLElist([1,1,2,3]))