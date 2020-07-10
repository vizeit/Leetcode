def oddCells(n, m, indices):
    matrix = [[0 for i in range(m)] for j in range(n)]
    odd = 0
    for k in indices:
        for i in range(m):
            matrix[k[0]][i] += 1
            odd = odd + 1 if matrix[k[0]][i] % 2 else odd - 1
        for j in range(n):
            matrix[j][k[1]] += 1
            odd = odd + 1 if matrix[j][k[1]] % 2 else odd - 1 
    return odd

if __name__ == "__main__":
    print(oddCells(2, 3, [[0,1],[1,1]]))
    print(oddCells(2, 2, [[1,1],[0,0]]))
            
