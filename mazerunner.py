import random,sys, time, math
from PIL import Image
from mpi4py import MPI


zawarudo = MPI.COMM_WORLD
myrank = zawarudo.Get_rank()



size = int(sys.argv[1])
maze = [[0 for x in range (size)] for y in range(size)]
image = Image.new("RGB", (size,size))
pixels = image.load()

def createmaze():
	image = Image.new("RGB", (size,size))
	pixels = image.load()
	#direcoes de movimento
	dx=[0,1,0,-1] #movimentacao no eixo x
	# =[S,E,N,W]
	dy=[-1,0,1,0] #movimentacao no eixo y
	color=[(0,0,0), (255,255,255), (0,255,0), (0,0,255)]
	#primeira celula:
	cx = 0; cy = 0
	maze[0][0] = 1 #marca a primeira celula
	maze[size-1][size-1] = 2
	stack = [(cx,cy,0)] #pos x, pos y, dir

	while len(stack)>0:
		dirRange = range(4)
		nlst=[]
		(cx,cy,cd) = stack[-1]
		vizinhos_livres=[] #lista de vizinhos disponiveis
		for i in dirRange: #procurando nas 4 direcoes
			nx = cx+dx[i] ; ny = cy+dy[i] #nx e ny sao as coord do no candidato
			#print("Looking at ("+str(nx)+","+str(ny)+")")
			if nx >=0 and nx<size and ny>=0 and ny<size:
				if maze[ny][nx]==0: #se a celula estiver livre
					vizinhos_ocupados = 0 #numero de vizinhos ocupados deve ser 1
					for j in range(4):#procurando vizinhos nas 4 direcoes
						vizinho_x = nx+dx[j]; vizinho_y = ny+dy[j] #ex sao os vizinhos do no candidato
			#			print("Looking at ("+str(vizinho_x)+","+str(vizinho_y)+")")
						if vizinho_x>=0 and vizinho_x<size and vizinho_y>=0 and vizinho_y<size:
							if maze[vizinho_y][vizinho_x] ==1: vizinhos_ocupados+=1
				if vizinhos_ocupados == 1: nlst.append(i)

		#se tiver um ou mais vizinhos livres, escolhe um aleatorio

		if len(nlst)>0:
			ir = nlst[random.randint(0,len(nlst)-1)]
			cx += dx[ir]; cy+=dy[ir]; maze[cy][cx]=1
			print("Walking to ("+str(cx)+","+str(cy)+")")
			stack.append((cx,cy,ir))
		else:stack.pop()

	for ky in range(size):
	    for kx in range(size):
	        pixels[kx, ky] = color[maze[size * ky / size][size * kx / size]]
	image.save("Maze.png", "PNG")

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0


    print ("start at "+str(start_node.position))
    print ("end at "+str(end_node.position))
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
       
        current_index = myrank


        '''
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
		'''

        # Pop current off open list, add to closed list
        current_node = open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            
            
            while current is not None:
                print ("entering node "+str(current.position)+";")
                path.append(current.position)
                maze[(current.position[0])][(current.position[1])] = 3 + myrank
                current = current.parent
            	
            return path[::-1] # Return reversed path

        # Generate children
        

       	children = []
       	for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
       	    # Get node position
       	    node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
       	    # Make sure within range
       	    if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
       	        continue
       	    # Make sure walkable terrain
       	    if maze[node_position[0]][node_position[1]] == 0:
       	        continue
       	    # Create new node
       	    new_node = Node(current_node, node_position)
       	    # Append
       	    children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            
            #print ("considering node "+str(child.position)+";")
            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = math.sqrt(((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    #child = open_list[random.randint(0,(len(open_list)-1))]
                    continue

            # Add the child to the open list
            open_list.append(child)

        if myrank == 0:
        	open_list = zawarudo.gather(open_list, root =0)
        	open_list.sort(reverse=True, key=lambda x: x.f)
        else: open_list = None; assert open_list is None

        open_list = zawarudo.scatter(open_list, root =0)
        

def paintsolution():
	#direcoes de movimento
	dx=[0,1,0,-1] #movimentacao no eixo x
	# =[S,E,N,W]
	maze[size-1][size-1]=2
	dy=[-1,0,1,0] #movimentacao no eixo y
	color=[(0,0,0), (255,255,255), (0,255,0), (255,0,255)]
	the_world = zawarudo.Get_size()
	for i in range(the_world):
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		newcolor = (r,g,b)
		color.append(newcolor)

	for ky in range(size):
	    for kx in range(size):
	        pixels[kx, ky] = color[maze[size * ky / size][size * kx / size]]
	image.save("Maze_solved.png", "PNG")

def main():
	print("Lets RUN!")
	
	if myrank is not 0:
		maze = None
	if myrank is 0:
		timestart1 = time.clock()
		createmaze()
		timend1 = time.clock()
		creation_time = timend1 - timestart1

	#scatter do labirinto original
	start = (0,0)
	end = ((size-1),(size-1))

	maze = zawarudo.scatter(maze, root=0)

	######################################
	zawarudo.barrier()
	runstart[myrank] = time.clock()
	
	path = astar(maze,start,end)
	
	runend[myrank] = time.clock()
	zawarudo.barrier()

	if myrank is 0: print ("Time it took to generate a "+str(size)+"x"+str(size)+" maze: "+str(creation_time)+"s \n")
	totaltime[myrank] = runend[myrank] - runstart[myrank]
	print("Node "+str(myrank)+" took "+str(totaltime[myrank])+" to run the maze")
	

	

	paintsolution()
	
if __name__ == '__main__':
	main()
