
'''
This program allows to identify position of two numbers in a given
list that when added together fulfills the target sum 
e.g. input numbers 2, 7, 8, 9 and 
for target sum 15 expected result is 1 , 2 
for target sum 17 expected result is 2 , 3
T(n) = O(n)
'''
#accept user input for the list of numbers
input_nums = input("Enter comma separated list of numbers: ")
num = eval(input_nums)

#accept user input for the target sum
input_target = input("Enter target sum: ")
target = int(input_target)

#define empty dictionary object
dic = {}

#loop through each number, subtract target with indexed num 
# to identify other num to complete the target sum
for i in range(0, len(num)):
    if dic.get(target-num[i]) == None:
        dic.update({num[i] : i})
    else:
        print(dic.get(target-num[i]), ',', i)
        break
     
