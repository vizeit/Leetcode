def removeOuterParentheses(S):
    sm = 0
    rs = ''
    for c in S:
        if sm != 0 and not (sm == 1 and c == ')') :
            rs += c
        sm = sm + 1 if c == '(' else sm - 1
    return rs

if __name__ == "__main__":
    print(removeOuterParentheses("()()"))