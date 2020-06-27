def reverse(x: int) -> int:
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:
    Input: 123
    Output: 321

    Example 2:
    Input: -123
    Output: -321

    Example 3:
    Input: 120
    Output: 21

    Note:
    Assume we are dealing with an environment which could only store 
    integers within the 32-bit signed integer range: [−231,  231 − 1]. 
    For the purpose of this problem, assume that your function returns 0 
    when the reversed integer overflows.
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    r = sum(n*10**i for i, n in enumerate(map(int, ascii(abs(x)))))
    return 0 if r > INT_MAX or r < INT_MIN else r if x > 0 else -r

if __name__ == "__main__":
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))