def medianofarray(ll, lr):
    m = (len(ll)+len(lr)) // 2
    l = []
    i = j = 0
    while (i < len(ll) or j < len(lr)) and len(l) <= m:
        if i == len(ll):
            l.append(lr[j])
            j += 1
        elif j == len(lr):
            l.append(ll[i])
            i += 1
        elif ll[i] < lr[j]:
            l.append(ll[i])
            i += 1
        else:
            l.append(lr[j])
            j += 1
    return float(l[m]) if (len(ll)+len(lr)) % 2 else (l[m-1] + l[m]) / 2

if __name__ == "__main__":
    print(medianofarray([1,2],[3,4])) 