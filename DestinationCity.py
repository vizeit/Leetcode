def destCity(paths):
    sc = set()
    dc = set()
    for path in paths:
        sc.add(path[0])
        if path[1] not in sc:
            dc.add(path[1])
        if path[0] in dc:
            dc.remove(path[0])
    return dc.pop()
if __name__ == "__main__":
    print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
    print(destCity([["B","C"],["D","B"],["C","A"]]))
    print(destCity([["A","Z"]]))

        