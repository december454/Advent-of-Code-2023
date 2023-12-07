# Advent of Code 2032
# Day 1: Trebuchet?!
# Part 1

import fileinput

sum = 0

for line in fileinput.input(files = 'input.txt'):
    digits = ''.join(i for i in line if i.isdigit())
    firstAndLast = digits[0] + digits[len(digits) - 1]
    sum += int(firstAndLast)
    
print(sum)