def subtractProductAndSum(n: int) -> int:
    if n == 0:
        return 0
    su,pr = 0, 1
    while n:
        n, d = divmod(n,10)
        su += d
        pr *= d
    return pr - su

if __name__ == "__main__":
    print(subtractProductAndSum(234))