from functools import reduce
from operator import mul
def subtractProductAndSum(n: int) -> int:
    return reduce(mul, map(int, ascii(n))) - sum(map(int, ascii(n)))

if __name__ == "__main__":
    print(subtractProductAndSum(234))