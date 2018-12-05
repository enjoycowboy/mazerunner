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
	color=[(0,0,0), (255,255,255)]
	#primeira celula:
	cx = 0; cy = 0
	maze[cy][cx] = 1 #marca a primeira celula
	maze[size-1][size-1] = 1
	stack = [(cx,cy,0)] #pos x, pos y, dir

	while len(stack)>0:
		dirRange = range(4)
		nlst=[]
		(cx,cy,cd) = stack[-1]
		vizinhos_livres=[] #lista de vizinhos disponiveis
		for i in dirRange: #procurando nas 4 direcoes
			nx = cx+dx[i] ; ny = cy+dy[i] #nx e ny sao as coord do no candidato
			print("Looking at ("+str(nx)+","+str(ny)+")")
			if nx >=0 and nx<size and ny>=0 and ny<size:
				if maze[ny][nx]==0: #se a celula estiver livre
					vizinhos_ocupados = 0 #numero de vizinhos ocupados deve ser 1
					for j in range(4):#procurando vizinhos nas 4 direcoes
						vizinho_x = nx+dx[j]; vizinho_y = ny+dy[j] #ex sao os vizinhos do no candidato
						print("Looking at ("+str(vizinho_x)+","+str(vizinho_y)+")")
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




def solvemaze(maze, size):
	dx = [0,1,0,-1]; dy = [-1,0,1,0]
	color = [(0,0,0),(255,255,255),(255,0,255)]
	cx =0 ; cy=0 #comecando em 0,0
	stack = [(0,0,0)]
	steps= [[0 for x in range(size)] for y in range(size)]
	dirRange = range(4)
	valid_steps=[]
	current_x = 0
	current_y = 0
	while len(stack) > 0:
		(current_x, current_y,cd) = stack[-1]
		for i in dirRange:
			next_x = current_x + dx[i]; next_y = current_y + dy[i] 			# espaco em branco  -> maze[x][y] = 1
			print("Looking at ("+str(next_x)+","+str(next_y)+")")
			if next_x >= 0 and next_x < size and next_y >= 0 and next_y < size:
				if maze[next_y][next_x] == 1:
					ctr = 0
					for j in range(4): #profundidade
						ex = next_x + dx[j]; ey= next_y + dy[j]
						if ex >= 0 and ex < size and ey >= 0 and ey < size:
							if maze[ey][ex] == 1: ctr+=1
					if ctr == 1: valid_steps.append(i);

		if len(valid_steps) > 0:
			direction = valid_steps[random.randint(0, len(valid_steps)-1)]
			current_x += dx[direction]; current_y += dy[direction]; maze[current_y][current_x] = 3
			print("Walking to ("+str(cx)+","+str(cy)+")")
			stack.append((current_y,current_x,direction))
		else: stack.pop()

	return steps

#solution = list of steps taken
#def metrics(solution):


def main():
	print ("lets run!")
	size = 1000
	run = [[]]
	steps = [[]]

	color = [(0,0,0),(255,0,0)]
		
	try:
		run = createmaze(size)
		image = Image.open("Maze.png")
		pixels = image.load()
		sys.stdout.flush()
		print("maze created! running....")
		time.sleep(5)
		steps = solvemaze(run,size)
	except KeyboardInterrupt:
		
		
		for ky in range(size):
			for kx in range(size):
				pixels[kx, ky] = color[steps[size * ky / size][size * kx / size]]
	
		image.save("Solution_" + str(size) + "x" + str(size) + ".png", "PNG")
		exit(0)
	

if __name__ == '__main__':
	main()

