def Longestsubstring():
    """
    This program allows to find longest substring within a input string
    without repeating characters
    e.g. input: "abcabcbb"
    output: 3
    explanation: the answer is "abc", length 3
    T(n) = O(n)
    """

    #accept user input for the string
    s = input("Enter the string: ")
    ml = 0
    st = set()
    for i in range(len(s)):
        if ml >= len(s) - i:
            break
        for j in range(i,len(s)):
            if s[j] in st:
                ml = len(st) if len(st) > ml else ml
                st.clear()
                break
            else:
                st.add(s[j])
    ml = len(st) if st and len(st) > ml else ml 
    return ml

if __name__ == "__main__":
    print(Longestsubstring())