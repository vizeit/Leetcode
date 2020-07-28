def peakIndexInMountainArray(A):
    if len(A) < 2: return 0
    low, high = 0, len(A)-1
    while low <= high:
        mid = (low+high)//2
        if A[low] > A[low+1]:
            return low
        elif A[high] > A[high-1]:
            return high
        elif A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            return mid
        elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
            low = mid+1
        else:
            high = mid-1
    return mid

if __name__ == "__main__":
    try:
        assert peakIndexInMountainArray([0,1,0])==1, "1st test case failed"
        assert peakIndexInMountainArray([0,2,1,0])==1, "2nd test case failed"
    except AssertionError as err:
        print(err)