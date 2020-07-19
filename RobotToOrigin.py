def judgeCircle(moves):
    return sum(1 if c == 'U' else -1 if c == 'D' else 2 if c == 'L' else -2 for c in moves) == 0

if __name__ == "__main__":
    print(judgeCircle("UD"))
    print(judgeCircle("LL"))