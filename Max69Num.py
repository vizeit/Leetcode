from math import log10
def maximum69Number(num):
    d = int(log10(num))
    n = num
    while n:
        digit, n = divmod(n, 10**d)
        if digit == 6:
            return num + 3*10**d
        d -= 1
    return num
if __name__ == "__main__":
    print(maximum69Number(9669))
    print(maximum69Number(9996))
    print(maximum69Number(9999))
    print(maximum69Number(66))