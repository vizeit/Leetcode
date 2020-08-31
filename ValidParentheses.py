def isValid(s):
    stack = []
    for c in s:
        if c == ')':
            if not stack or '(' != stack.pop(): return False
        elif c == ']':
            if not stack or '[' != stack.pop(): return False
        elif c == '}':
            if not stack or '{' != stack.pop(): return False
        else:
            stack.append(c)
    return True if not stack else False

if __name__ == "__main__":
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("([)]"))
    print(isValid("{[]}"))
    print(isValid("{"))
    print(isValid("(("))
    print(isValid("(()}"))