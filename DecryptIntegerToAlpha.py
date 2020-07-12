def freqAlphabets(s):
    i = len(s)
    rs=''
    while i:
        i -= 1
        if s[i] == '#':
            rs = chr(int(s[i-2:i])+96)+rs
            i -= 2
        else:
            rs = chr(int(s[i])+96)+rs
    return rs

if __name__ == "__main__":
    print(freqAlphabets("10#11#12"))
    print(freqAlphabets("1326#"))
    print(freqAlphabets("25#"))
    print(freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))