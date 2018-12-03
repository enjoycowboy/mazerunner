#producer
# Random Maze Generator using Depth-first Search
# http://en.wikipedia.org/wiki/Maze_generation_algorithm

import sys
import random
from PIL import Image
imgx = 500; imgy = 500
image = Image.new("RGB", (imgx, imgy))
pixels = image.load()
xmax = 100; ymax = 100 # width and height of the maze
maze = [[0 for x in range(xmax)] for y in range(ymax)]
dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
color = [(0, 0, 0), (255, 255, 255)] # RGB colors of the maze
# start the maze from a random cell
xcurrent = random.randint(0, xmax - 1); ycurrent = random.randint(0, ymax - 1)
maze[ycurrent][xcurrent] = 1; stack = [(xcurrent, ycurrent, 0)] # stack element: (x, y, direction)

while len(stack) > 0:
    (xcurrent, ycurrent, cd) = stack[-1]
    # to prevent zigzags:
    # if changed direction in the last move then cannot change again
    if len(stack) > 2:
        if cd != stack[-2][2]: dirRange = [cd]
        else: dirRange = range(4)
    else: dirRange = range(4)

    # find a new cell to add
    nlst = [] # list of available neighbors
    for i in dirRange:	#procura em todas as direcoes; dirRange = (0,1,2,3)
        nx = xcurrent + dx[i]; ny = ycurrent + dy[i] #proximo no
        if nx >= 0 and nx < xmax and ny >= 0 and ny < ymax: #se o proximo no ta dentro da imagem
            if maze[ny][nx] == 0: #se estiver disponivel
                ctr = 0 # of occupied neighbors must be 1
                for j in range(4): #nas quatro direcoes
                    ex = nx + dx[j]; ey = ny + dy[j]
                    if ex >= 0 and ex < xmax and ey >= 0 and ey < ymax:  #se ta dentro da img
                        if maze[ey][ex] == 1: ctr += 1 #se ta disponivel, incrementa o contador
                if ctr == 1: nlst.append(i) #so incrementa a lista se tiver exatamente 1 vizinho livre

    # if 1 or more neighbors available then randomly select one and move
    if len(nlst) > 0:
        ir = nlst[random.randint(0, len(nlst) - 1)]
        xcurrent += dx[ir]; ycurrent += dy[ir]; maze[ycurrent][xcurrent] = 1
        stack.append((xcurrent, ycurrent, ir))
    else: stack.pop()

# paint the maze
for ky in range(imgy):
    for kx in range(imgx):
        pixels[kx, ky] = color[maze[ymax * ky / imgy][xmax * kx / imgx]]
image.save("Maze_" + str(xmax) + "x" + str(ymax) + ".png", "PNG")
file = open("maze_output.txt", "w");

for jj in range(ymax):
    for ii in range(xmax):
        file.write(str(maze[jj][ii]))
        ii +=1
    jj+=1
    file.write("\n")
file.close()

print("ok!")
