#Conway's Game of Life
#Conway's Game of Life is an Example of Cellular automata
# Rules of Conway’s Game of Life
#1- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#2- Any live cell with two or three live neighbours lives on to the next generation.
#3- Any live cell with more than three live neighbours dies, as if by overpopulation.
#4- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
import random, time, copy
WIDTH = 4
HEIGHT = 13
alive = '#'
dead = ' '

#Create a list of list for the cells:
conway_graph = []
for i in range(HEIGHT):
    row = [] #Create a new row.
    for j in range(WIDTH):
        if(random.randint(0,1)==0):
           row.append(alive) # add a living cell.
        else:
            row.append(dead) # add a dead cell.
    print(row)
    conway_graph.append(row) # conway_graph is a list of cloumn list.

while True: # Main program loop
    print('\n\n\n') #
    currentGraphState = copy.deepcopy(conway_graph)

    #Print currentCells on the screen:
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print('|',currentGraphState[i][j],'|', end='') # print # and space in a row format
        print() # print a newline at the end of the row.

    #Calculate the Next State of the conway's graph based on the current state.
    for i in range(HEIGHT):
        for j in range(WIDTH):
            #Get neighboring coordinates:
            # '% WIDTH' ensure leftCoord is always between 0 and WIDTH-1
            leftCoord = (j-1) % WIDTH
            rightCoord = (j+1)%WIDTH 
            aboveCoord = (i-1)%HEIGHT
            belowCoord = (i+1)%HEIGHT

            #count number of living neighbors:
            numNeighbors=0
            if currentGraphState[aboveCoord][leftCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentGraphState[aboveCoord][j] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentGraphState[aboveCoord][rightCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentGraphState[i][leftCoord] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentGraphState[i][rightCoord] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentGraphState[belowCoord][leftCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentGraphState[belowCoord][j] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentGraphState[belowCoord][rightCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.
            
            # Set cell based on Conway's Game of Life rules:
            if currentGraphState[i][j]== '#' and (numNeighbors == 2 or
            numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                conway_graph[i][j] = '#'
            elif currentGraphState[i][j] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                conway_graph[i][j] = '#'
            else:
                # Everything else dies or stays dead:
                conway_graph[i][j] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.
