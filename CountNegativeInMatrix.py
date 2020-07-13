def countNegatives(grid):
    ct = 0
    for r in grid:
        for i in range(len(r)-1, -1, -1):
            if r[i] < 0: ct+=1
            else: break
    return ct
if __name__ == "__main__":
    print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    print(countNegatives([[3,2],[1,0]]))
    print(countNegatives([[1,-1],[-1,-1]]))
    print(countNegatives([[-1]]))
