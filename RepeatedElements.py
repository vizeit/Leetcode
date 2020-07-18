from collections import defaultdict
def repeatedNTimes(A):
    d = defaultdict(int)
    for i in A:
        d[i] += 1
        if d[i] == len(A)//2: return i

if __name__ == "__main__":
    print(repeatedNTimes([1,2,3,3]))
    print(repeatedNTimes([2,1,2,5,3,2]))
    print(repeatedNTimes([5,1,5,2,5,3,5,4]))