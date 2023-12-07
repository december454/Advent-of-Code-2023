# Advent of Code 2032
# Day 1: Trebuchet?!
# Part 2

import fileinput

sum = 0

numberDict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
numberList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in fileinput.input(files = 'input.txt'):
    firstAndLast = ['',''];
    firstIndex = len(line) - 1
    lastIndex = 0
    
    # Find first and last occurrances of string numbers, if any.
    for numberString in numberList:
        f_index = line.find(numberString)
        l_index = line.rfind(numberString)
        
        if f_index < firstIndex and f_index > -1:
            firstIndex = f_index
            
        if l_index > lastIndex:
            lastIndex = l_index
        
    # Check if there are any actual digits which came before or after the string numbers.
    for i in range(firstIndex):
        if line[i].isdigit():
            firstAndLast[0] = line[i]
            firstIndex = -1
            break
            
    for i in range(len(line) - 1, lastIndex - 1, -1):
        if line[i].isdigit():
            firstAndLast[1] = line[i]
            lastIndex = -1
            break
    
    # If the first occurrance of a number was via a number string.
    if firstIndex > -1:
        for numberString in numberList:
            if line.find(numberString) == firstIndex:
                firstAndLast[0] = numberDict[numberString]
                break
                
    # If the last occurrance of a number was via a number string.
    if lastIndex > -1:
        for numberString in numberList:
            if line.rfind(numberString) == lastIndex:
                firstAndLast[1] = numberDict[numberString]
                break
    
    # Debug Output
    # print('------------------------------------------')
    # print(line)
    # print(int(firstAndLast[0] + firstAndLast[1]))
    # print('------------------------------------------')
         
    sum += int(firstAndLast[0] + firstAndLast[1])
    
print(sum)