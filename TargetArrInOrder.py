def createTargetArray(nums, index):
    rs = []
    for i, j in zip(nums, index):
        rs.insert(j, i)
    return rs

if __name__ == "__main__":
    print(createTargetArray([0,1,2,3,4], [0,1,2,2,1]))
    print(createTargetArray([1,2,3,4,0], [0,1,2,3,0]))
    print(createTargetArray([1,3,2,4,0], [0,1,2,3,0]))