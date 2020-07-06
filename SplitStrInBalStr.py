def balancedStringSplit(s: str) -> int:
    su = 0
    cnt = 0
    for c in s:
        su = su + 1 if c == 'R' else su - 1
        if su == 0:
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(balancedStringSplit("RLRRLLRLRL"))
    print(balancedStringSplit("RLLLLRRRLR"))
    print(balancedStringSplit("LLLLRRRR"))
    print(balancedStringSplit("RLRRRLLRLL"))