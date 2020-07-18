def sortArrayByParity(A):
    if len(A) < 2: return A
    forward, backward = 0, len(A)-1
    while forward < backward:
        if A[forward] % 2 and not A[backward] % 2:
            A[forward], A[backward] = A[backward], A[forward]
            forward += 1
            backward -= 1
        elif not A[forward] % 2 and A[backward] % 2:
            forward += 1
            backward -= 1
        elif not A[forward] % 2 and not A[backward] % 2:
            forward += 1
        else:
            backward -= 1
    return A

if __name__ == "__main__":
    print(sortArrayByParity([1,3,2,4]))
    print(sortArrayByParity([3,1,2,4]))