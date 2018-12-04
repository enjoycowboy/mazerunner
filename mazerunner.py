import random, signal
from PIL import Image

def createmaze(size):
	image = Image.new("RGB", (size,size))
	pixels = image.load()
	maze = [[0 for x in range (size)] for y in range(size)]
	#direcoes de movimento
	dx=[0,1,0,-1] #movimentacao no eixo x
	# =[S,E,N,W]
	dy=[-1,0,1,0] #movimentacao no eixo y
	color=[(0,0,0), (255,255,255)]
	#primeira celula:
	cx = 0; cy = 0
	maze[cy][cx] = 1 #marca a primeira celula
	stack = [(cx,cy,0)] #pos x, pos y, dir

	while len(stack)>0:
		dirRange = range(4)
		nlst=[]
		(cx,cy,cd) = stack[-1]
		vizinhos_livres=[] #lista de vizinhos disponiveis
		for i in dirRange: #procurando nas 4 direcoes
			nx = cx+dx[i] ; ny = cy+dy[i] #nx e ny sao as coord do no candidato
			if nx >=0 and nx<size and ny>=0 and ny<size:
				if maze[ny][nx]==0: #se a celula estiver livre
					vizinhos_ocupados = 0 #numero de vizinhos ocupados deve ser 1
					for j in range(4):#procurando vizinhos nas 4 direcoes
						vizinho_x = nx+dx[j]; vizinho_y = ny+dy[j] #ex sao os vizinhos do no candidato
						if vizinho_x>=0 and vizinho_x<size and vizinho_y>=0 and vizinho_y<size:
							if maze[vizinho_y][vizinho_x] ==1: vizinhos_ocupados+=1
				if vizinhos_ocupados == 1: nlst.append(i)

		#se tiver um ou mais vizinhos livres, escolhe um aleatorio

		if len(nlst)>0:
			ir = nlst[random.randint(0,len(nlst)-1)]
			cx += dx[ir]; cy+=dy[ir]; maze[cy][cx]=1
			stack.append((cx,cy,ir))
		else:stack.pop()

	for ky in range(size):
	    for kx in range(size):
	        pixels[kx, ky] = color[maze[size * ky / size][size * kx / size]]
	image.save("Maze_" + str(size) + "x" + str(size) + ".png", "PNG")

	return maze



def solvemaze(maze, size):
	dx = [0,1,0,-1]; dy = [-1,0,1,0]
	color = [(0,0,0),(255,255,255),(255,0,255)]
	cx =0 ; cy=0 #comecando em 0,0
	stack = [(0,0,0)]
	steps= [[]]
	dirRange = range(4)
	nlst=[]
	while len(stack) > 0:
		
		# espaco em branco  -> maze[x][y] = 1
		# parede 			-> maze[x][y] = 0
		# caminho andado    -> maze[x][y] = 7
		# começa de algum canto.
		# olhar nas quatro direcoes
		# criar lista de caminhos possiveis
			# se maze[x][y] == 0 nao appenda
			# se maze[x][y] == 1 appenda na lista de proximo no possivel
			# se tiver mais do que um nó na lista 
				# analisa se tem algum marcado com 7
				# se tiver vai pra outro canto
				# se nao tiver, toma uma direcao aleatoria
			#quando tiver um caminho possivel so, coloca na lista de passos (stack)



		# evitar backtrack

	for ky in range(size):
	    for kx in range(size):
	        pixels[kx, ky] = color[steps[size * ky / size][size * kx / size]]
	
	image.save("Solution_" + str(size) + "x" + str(size) + ".png", "PNG")



#solution = list of steps taken
#def metrics(solution):


def main():
	print ("lets run!")
	size = 1000
	run = [[]]
	steps = [[]]
	image = Image.new("RGB", (size,size))
	pixels = image.load()
	color = [(0,0,0),(255,0,0)]
		
	try:
		run = createmaze(size)
		steps = solvemaze(run,size)
	except KeyboardInterrupt:
		for ky in range(size):
			for kx in range(size):
				pixels[kx, ky] = color[steps[size * ky / size][size * kx / size]]
	
		image.save("Solution_" + str(size) + "x" + str(size) + ".png", "PNG")
		exit(0)
	

if __name__ == '__main__':
	main()

