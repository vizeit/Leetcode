
def generateTheString(n):
    return 'x'*n if n % 2 else 'x'*(n-1)+'y'

if __name__ == "__main__":
    print(generateTheString(2))
    print(generateTheString(1))
    print(generateTheString(7))
    print(generateTheString(8))