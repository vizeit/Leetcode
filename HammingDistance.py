def hammingDistance(x: int, y: int) -> int:
    x = x ^ y
    y = 0
    while x:
        if x & 1: y+=1
        x = x>>1
    return y

if __name__ == "__main__":
    print(hammingDistance(1, 4))
    print(hammingDistance(1374, 56889))
    print(hammingDistance(47584, 78789))