def main():
    """
    This program allows to add two numbers provided in reverse order
    and print the digits of the sum in reverse order
    e.g. input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    output: 7 -> 0 -> 8
    explanation: 342 + 465 = 807
    T(n) = O(n)
    """
    #accept user input for the 1st number
    input_nums = input("Enter comma separated reverse ordered digits of 1st number: ")
    set_1 = eval(input_nums)
    #accept user input for the 2nd number
    input_nums = input("Enter comma separated reverse ordered digits of 2nd number: ")
    set_2 = eval(input_nums)

    output = []

    #iterate through each digits in the two numbers to sum
    for i in range(0 , len(set_1)):
        if set_1[i] + set_2[i] >= 10:
            if i < len(output):
                output[i] += ((set_1[i] + set_2[i]) - 10)
                output.append(1)
            else:
                output.append(((set_1[i] + set_2[i]) - 10))
                output.append(1)
        else:
            if i < len(output):
                output[i] += set_1[i] + set_2[i]
            else:
                output.append(set_1[i] + set_2[i])
            
    print(output)

if __name__ == "__main__":
    main()