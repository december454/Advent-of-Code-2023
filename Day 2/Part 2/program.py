# Advent of Code 2032
# Day 2: Cube Conundrum 
# Part 2

import fileinput

sum = 0

for line in fileinput.input(files = 'input.txt'):    
    line = line.split(':');
    gameNumber = int((line[0])[5:])
    gameRounds = line[1].split(';')
    
    rMin = 0
    gMin = 0
    bMin = 0
    
    for gameRound in gameRounds:               
        cubeDraws = gameRound.split(',')

        for cubeDraw in cubeDraws: 
            cubeDraw = cubeDraw.split()
            
            numberDrawn = int(cubeDraw[0])
            colorDrawn = cubeDraw[1]
            
            if colorDrawn == 'red' and numberDrawn > rMin:                                
                rMin = numberDrawn
            if colorDrawn == 'green' and numberDrawn > gMin:
                gMin = numberDrawn
            if colorDrawn == 'blue' and numberDrawn > bMin:                                
                bMin = numberDrawn                    
            

    power = rMin * gMin * bMin
    
    sum += power    
    print ("Game: " + str(gameNumber) + " Power: " + str(power) + " Sum: " + str(sum))
        
    
print(sum)