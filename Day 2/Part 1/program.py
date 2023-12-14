# Advent of Code 2032
# Day 2: Cube Conundrum 
# Part 1

import fileinput

sum = 0

rMax = 12
gMax = 13
bMax = 14

for line in fileinput.input(files = 'input.txt'):    
    line = line.split(':');
    gameNumber = int((line[0])[5:])
    gamePossible = True
    gameRounds = line[1].split(';')
    
    for gameRound in gameRounds:            
        cubeDraws = gameRound.split(',')

        for cubeDraw in cubeDraws: 
            cubeDraw = cubeDraw.split()
            
            numberDrawn = int(cubeDraw[0])
            colorDrawn = cubeDraw[1]
            
            if colorDrawn == 'red' and numberDrawn > rMax:
                print("Game: " + str(gameNumber) + " Not Possible. Red: " + str(numberDrawn) + " > " + str(rMax))
                gamePossible = False
                break
            if colorDrawn == 'green' and numberDrawn > gMax:
                print("Game: " + str(gameNumber) + " Not Possible. Green: " + str(numberDrawn) + " > " + str(gMax))
                gamePossible = False
                break
            if colorDrawn == 'blue' and numberDrawn > bMax:
                print("Game: " + str(gameNumber) + " Not Possible. Blue: " + str(numberDrawn) + " > " + str(bMax))
                gamePossible = False
                break                           
            
            # print(cubeDraw[0])
            # print(cubeDraw[1])
            
        if not gamePossible:            
            break
    
    if gamePossible: 
        sum += gameNumber    
        print ("Game: " + str(gameNumber) + " Succeeded. Sum: " + str(sum))
        
    
print(sum)