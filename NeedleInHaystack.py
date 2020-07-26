def strStr(haystack: str, needle: str) -> int:
    n = len(needle)
    if n==0:return 0
    for i in range(len(haystack)):
        if haystack[i:i+n]==needle:
            return i
    return -1

if __name__ == "__main__":
    print(strStr('hello','ll'))
    print(strStr('aaaaa','bba'))