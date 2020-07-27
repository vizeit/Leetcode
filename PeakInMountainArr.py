def peakIndexInMountainArray(A):
    if len(A) < 2: return 0
    for i in range(len(A)-1):
        if A[i+1] <= A[i]:
            return i
    return i+1

if __name__ == "__main__":
    try:
        assert peakIndexInMountainArray([0,1,0])==1, "1st test case failed"
        assert peakIndexInMountainArray([0,2,1,0])==1, "2nd test case failed"
    except AssertionError as err:
        print(err)