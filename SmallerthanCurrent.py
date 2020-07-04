def smallerNumbersThanCurrent(nums):
    rs = []
    for i in nums:
        su = sum(1 for j in nums if j < i)
        rs.append(su)
    return rs
if __name__ == "__main__":
    print(smallerNumbersThanCurrent([8,1,2,2,3]))