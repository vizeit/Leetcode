from functools import reduce
from operator import xor
def xorOperation(n: int, start: int) -> int:
    return reduce(xor, [start+2*i for i in range(n)])

if __name__ == "__main__":
    print(xorOperation(5, 0))
    print(xorOperation(4, 3))
    print(xorOperation(1, 7))
    print(xorOperation(10, 5))