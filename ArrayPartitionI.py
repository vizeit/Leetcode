def arrayPairSum(nums):
    return sum(sorted(nums)[::2])

if __name__ == "__main__":
    print(arrayPairSum([-1,-3,-8,-4]))
    print(arrayPairSum([1,4,3,2]))