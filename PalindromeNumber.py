def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    n = []
    while x:
        x, i = divmod(x, 10)
        n.append(i)
    return n == n[::-1]
if __name__ == "__main__":
    print(isPalindrome(12))