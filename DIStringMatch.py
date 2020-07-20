def diStringMatch(S):
    minmax = [0,len(S)]
    rs = []
    for c in S:
        if c == 'I':
            rs.append(minmax[0])
            minmax[0]+=1
        else:
            rs.append(minmax[1])
            minmax[1]-=1
    rs.append(minmax[1]) if c == 'I' else rs.append(minmax[0])
    return rs

if __name__ == "__main__":
    print(diStringMatch('IDID'))
    print(diStringMatch('DDI'))