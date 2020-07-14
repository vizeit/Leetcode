from itertools import chain
def sumZero(n):
    return list(range(n//2,-(n//2+1),-1)) if n%2 else list(chain(range(1,n//2+1),range(-1,-(n//2+1),-1)))

if __name__ == "__main__":
    print(sumZero(1))
    print(sumZero(2))
    print(sumZero(7))
    print(sumZero(60))
    print(sumZero(100))
    print(sumZero(1000))