import random, signal,sys, time
from PIL import Image

def createmaze(size):
	image = Image.new("RGB", (size,size))
	pixels = image.load()
	maze = [[0 for x in range (size)] for y in range(size)]
	#direcoes de movimento
	dx=[0,1,0,-1] #movimentacao no eixo x
	# =[S,E,N,W]
	dy=[-1,0,1,0] #movimentacao no eixo y
	color=[(0,0,0), (255,255,255), (0,255,0)]
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
			#print("Walking to ("+str(cx)+","+str(cy)+")")
			stack.append((cx,cy,ir))
		else:stack.pop()

	for ky in range(size):
	    for kx in range(size):
	        pixels[kx, ky] = color[maze[size * ky / size][size * kx / size]]
	image.save("Maze.png", "PNG")

	return maze

# parede 			-> maze[x][y] = 0
# caminho andado    -> maze[x][y] = 7
# comeca de algum canto.
# olhar nas quatro direcoes
# criar lista de caminhos possiveis
	# se maze[x][y] == 0 nao appenda
	# se maze[x][y] == 1 appenda na lista de proximo no possivel
	# se tiver mais do que um no na lista 
		# analisa se tem algum marcado com 7
		# se tiver vai pra outro canto
		# se nao tiver, toma uma direcao aleatoria
	#quando tiver um caminho possivel so, coloca na lista de passos (stack(
	#se for 0 nas quatro direcoes, quebra tudo e pula fora da func

def solvemaze(maze, x, y):
	
	if maze[x][y] == 2:
		return True

	elif maze[x][y] == 0:
		return False

	elif maze[x][y] == 3:
		return False

	print 'visiting %d,%d' % (x, y)

	maze[x][y] = 3
   # explore neighbors clockwise starting by the one on the right

	if ((x < len(maze)-1 and solvemaze(maze, x+1, y))
		or (y > 0 and solvemaze(maze, x, y-1))
		or (x > 0 and solvemaze(maze, x-1, y))
		or (y < len(maze)-1 and solvemaze(maze, x, y+1))):
		return True
	return False


#solution = list of steps taken
#def metrics(solution):


def main():
	size = int(sys.argv[1])
	print ("lets run!")
	run = [[]]
	steps = [[0 for x in range(size)] for y in range(size)]
	color = [(0,0,0),(255,255,255),(0,255,0),(0,0,255), (255,0,0)]
	try:
		run = createmaze(size)
		
		'''
		sys.stdout.flush()
		print("maze created! running....")
		time.sleep(5)
		'''

		steps = solvemaze(run,0,0)

		image = Image.open("Maze.png")
		pixels = image.load()
	except KeyboardInterrupt:
		exit(0)

	for ky in range(size):
			for kx in range(size):
				pixels[kx, ky] = color[run[size * ky / size][size * kx / size]]
	
	image.save("Solution_" + str(size) + "x" + str(size) + ".png", "PNG")
if __name__ == '__main__':
	main()

