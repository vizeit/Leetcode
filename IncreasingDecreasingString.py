from collections import Counter
from itertools import chain, cycle
def sortString(s):
    d = Counter(s)
    if len(d) < 2: return s
    lk = sorted(d.keys())
    s = ''
    for i in cycle(chain(range(0,len(lk)),range(len(lk)-1,-1,-1))):
        if lk[i] in d:
            s+=lk[i]
            d[lk[i]] -=1
            if d[lk[i]] == 0: del d[lk[i]]
        if len(d) == 0:
            break
    return s
if __name__ == "__main__":
    print(sortString('aaaabbbbcccc'))
    print(sortString('rat'))
    print(sortString('leetcode'))
    print(sortString('ggggggg'))
    print(sortString('spo'))