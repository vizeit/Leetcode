from collections import Counter
def smallerNumbersThanCurrent(nums):
    d = Counter(nums)
    pv = 0
    for i in sorted(d.keys()):
        pv, d[i] = d[i]+pv, pv
    return [d[j] for j in nums]
if __name__ == "__main__":
    print(smallerNumbersThanCurrent([7,7,7,7]))