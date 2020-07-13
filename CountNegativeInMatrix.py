from itertools import takewhile
def countNegatives(grid):
    return sum(1 for r in grid for i in takewhile(lambda x: x<0, r[::-1]))
if __name__ == "__main__":
    print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    print(countNegatives([[3,2],[1,0]]))
    print(countNegatives([[1,-1],[-1,-1]]))
    print(countNegatives([[-1]]))
