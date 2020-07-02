def numberOfSteps(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num % 2:
        return 2 + numberOfSteps(num//2)
    else:
        return 1 + numberOfSteps(num//2)

if __name__ == "__main__":
    print(numberOfSteps(2))