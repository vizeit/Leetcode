'''
This program allows to find longest substring within a input string
without repeating characters
e.g. input: "abcabcbb"
output: 3
explanation: the answer is "abc", length 3
T(n) = O(n)
'''

#accept user input for the string
input_str = input("Enter the string: ")

ln = 0
substr = ""
output = ""

for ch in input_str:
    if len(substr) == 0:
        substr = ch
    elif len(substr) == 1 and substr == ch:
        if len(substr) > ln:
            ln = len(substr)
            output = str(ln) + ' ' + substr
        substr = ""
    elif substr[-1] == ch or substr.find(ch) != -1:
        if len(substr) > ln:
            ln = len(substr)
            output = str(ln) + ' ' + substr
        substr = ch
    else:
        substr += ch

if len(substr) > ln:
    ln = len(substr)
    output = str(ln) + ' ' + substr

print(output)