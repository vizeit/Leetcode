def flipAndInvertImage(A):
    return [[j for j in map(lambda x: x-1 if x else x+1, i[::-1])] for i in A]

if __name__ == "__main__":
    print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
    print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
             