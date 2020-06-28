from math import log10
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    n = x
    for i in range(int(log10(x)),-1,-1):
        n, d = divmod(n, 10)
        x -= d * 10**i
    return x == 0
if __name__ == "__main__":
    print(isPalindrome(112))