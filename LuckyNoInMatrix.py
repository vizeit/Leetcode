def luckyNumbers(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0: return []
    elif len(matrix) == 1: return [min(matrix[0])]
    dmin = {}
    rs = []
    c, r = 0, 1
    isforward = True
    mx = (0, matrix[0][0])
    while c < len(matrix[0]):
        if matrix[r][c] > mx[1]:
            mx = (r, matrix[r][c])
        if r == len(matrix)-1 or r == 0:
            if mx[0] not in dmin: dmin[mx[0]] = min(matrix[mx[0]])
            if mx[1] == dmin[mx[0]]: rs.append(mx[1])
            c+=1
            mx = (r, matrix[r][c]) if c < len(matrix[0]) else mx
            isforward = not isforward
        r = r+1 if isforward else r-1
    return rs

if __name__ == "__main__":
    print(luckyNumbers([]))
    print(luckyNumbers([[],[]]))
    print(luckyNumbers([[1],[2]]))
    print(luckyNumbers([[76618,42558,65788,20503,29400,54116]]))
    print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
    print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
    print(luckyNumbers([[7,8],[1,2]]))