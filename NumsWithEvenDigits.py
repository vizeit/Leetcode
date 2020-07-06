from math import log10
def findNumbers(nums) -> int:
    return sum(1 for i in nums if not (int(log10(i))+1)%2)

if __name__ == "__main__":
    print(findNumbers([12,345,2,6,7896]))
    print(findNumbers([555,901,482,1771]))