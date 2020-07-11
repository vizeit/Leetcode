def destCity(paths):
    sc = set()
    dc = set()
    for path in paths:
        sc.add(path[0])
        dc.add(path[1])
    return (dc-sc).pop()
if __name__ == "__main__":
    print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
    print(destCity([["B","C"],["D","B"],["C","A"]]))
    print(destCity([["A","Z"]]))

        