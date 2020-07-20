def sortedSquares(A):
    i = 0
    j = len(A)-1
    rs=[]
    while i <= j:
        if abs(A[i]) > abs(A[j]):
            rs.append(A[i]**2)
            i+=1
        else:
            rs.append(A[j]**2)
            j-=1
    return rs[::-1]

if __name__ == "__main__":
    print(sortedSquares([-4,-1, 0, 3,10]))
    print(sortedSquares([-7,-3,2,3,11]))
    print(sortedSquares([-7,-6,-5,-4,-1]))