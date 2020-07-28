def lengthOfLastWord(s):
    s = s.rstrip()
    r = s.rfind(' ')
    return len(s)-1-r if r != -1 else len(s)

if __name__ == "__main__":
    print(lengthOfLastWord("Hello World"))