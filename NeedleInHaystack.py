def strStr(haystack: str, needle: str) -> int:
    n = len(haystack)
    m = len(needle)
    if n == 0 and m != 0: return -1 
    if m == 0: return 0
    #create jump dictionary for mismatch scenario
    jump = {}
    for c in range(m):
        jump[needle[c]] = c
    i = m - 1
    k = m - 1
    while i < n:
        if haystack[i] == needle[k]:
            if k == 0:
                return i
            else:
                k -= 1
                i -= 1
        else:
            j = jump.get(haystack[i], -1) #-1 if not found
            i += m - min(k, j+1) #k is at index less than j, jump m-k. otherwise at m - j+1
            k = m - 1 #initialize k back to m-1
    return -1

if __name__ == "__main__":
    print(strStr('mississippi','issi'))
    print(strStr('hello','ll'))
    print(strStr('aaaaa','bba'))