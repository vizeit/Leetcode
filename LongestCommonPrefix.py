def longestCommonPrefix(strs):
    if len(strs) == 0: return ''
    common = strs[0]
    for i in range(1, len(strs)):
        if len(common) == 0 or len(strs[i]) == 0 or common[0] != strs[i][0]:
            return ''
        t=''
        for j in range(len(common)):
            if j == len(strs[i]) or common[j] != strs[i][j]:
                break
            else:
                t+=common[j]
        common = t
    return common
if __name__ == "__main__":
    print(longestCommonPrefix(["dog","racecar","car"]))