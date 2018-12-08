import random, signal,sys, time, heapq
from PIL import Image

size = int(sys.argv[1])
maze = [[0 for x in range (size)] for y in range(size)]


def createmaze():
	image = Image.new("RGB", (size,size))
	pixels = image.load()
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


class Cell(object):
	def __init__ (self,x,y,reachable):
		self.reachable = reachable
		self.x = x
		self.y = y
		self.g = 0
		self.h = 0
		self.f = 0
		self.parent = None
# G -> custo de ir da celula inicial a destino
# H -> custo de ir a uma celula qualquer ao destino
# F = G + H

class Aestrela(Cell):
	def __init__(self):
		self.aberto = []
		heapq.heapify(self.aberto)
		self.fechado = set()
		self.cells = []
		self.grid_height = size
		self.grid_width = size

## buscar as celulas parede

def calculo_h (self,cell):
	return 10 * abs(cell.x-self.end.x) + abs(cell.y - self.end.y)
def get_path(self, maze):
	cell = self.end
	path = [(cell.x, cell.y)]
	while cell.parent is not self.start:
		cell = cell.parent
		path.append((cell.x, cell.y))
		maze[cell.y][cell.x]=3
		path.append((self.start.x, self.start.y))
		path.reverse()

	for x in range(len(path)):
		path[x] 

	return path

def atualiza_g_h(self, adjacente, cell):

	adjacente.g = cell.g + 10
	adjacente.h = self.calculo_h(adjacente)
	adjacente.parent = cell
	adjacente.f = adjacente.h + adjacente.g

def paint():
	image = Image.open("Maze.png") #manipula a imagem da solucao
	pixels = image.load()
	color = [(0,0,0),(255,255,255),(0,255,0),(0,0,255), (255,0,0)]#parede, caminho, inico, percorrido, fim
	for ky in range(size):
		for kx in range(size):
			pixels[kx, ky] = color[run[size * ky / size][size * kx / size]]
	image.save("Solution_" + str(size) + "x" + str(size) + ".png", "PNG")




def solvemaze(astar,start,end):

#Coloca a celula inicial no heap:

	current_cell = start

	astar.aberto = [start]
	
	current_cell.x
	current_cell.y

	while len(astar.aberto):
		current_cell = astar.aberto.pop(0)
		
		print("evaluating ("+str(current_cell.x)+","+str(current_cell.y)+")")
		astar.fechado.add(current_cell)
		if current_cell.x == size-1 and current_cell.y == size-1:
			path(astar)
			paint()
			break
		#captura adjacentes
		'''
		adj_cells = [astar.cells[(current_cell.x+1)* size + current_cell.y],
astar.cells[(current_cell.x)* size + current_cell.y - 1],
astar.cells[(current_cell.x-1)* size + current_cell.y],
astar.cells[current_cell.x * size + current_cell.y + 1]]
'''		#fetcha os adjacentes
		adj_cells = [astar.cells[int(current_cell.x+1)* size + current_cell.y],
						astar.cells[(current_cell.x)* size + current_cell.y - 1],
						astar.cells[(current_cell.x-1)* size + current_cell.y],
						astar.cells[current_cell.x * size + current_cell.y + 1]]

		for i in range(len(adj_cells)):
			if adj_cells[i].x > size or adj_cells[i].x < 0 and adj_cells[i].y > size or adj_cells[i].y < 0:
				del adj_cells[i]

		print("Indexed Cells:\n")
		for i in range(len(adj_cells)):
			print("("+str(adj_cells[i].x)+","+str(adj_cells[i].y)+"), "+str(adj_cells[i].reachable))

		
		for adj_cell in adj_cells:

			print("considering cell ("+str(adj_cell.x)+"),("+str(adj_cell.y)+")")

			if adj_cell.reachable and adj_cell not in astar.fechado: # se nao estiver nos fechados
				if (adj_cell.f, adj_cell) in astar.aberto: # confere se eh melhor do que antes
					astar.atualiza_g_h(adj_cell, current_cell)
					print ("g = "+ str(current_cell.g)+", h ="+str(current_cell.h))
				
		astar.aberto.sort(reverse = False, key= int(current_cell.f))

		for i in range(len(astar.aberto)):
			print("("+str(astar.aberto.x)+","+str(astar.aberto.y)+")")

def main():
	print("Lets RUN!")
	createmaze()


	start = Cell(0,0,True) #comeca na celula 0,0
	end = Cell(size-1,size-1, True)

	
	cells = [start]
	abertas = [start]
	for xx in range(size):
		for yy in range(size):
			if maze[yy][xx] == 0:
				reachable = False
				
			else: reachable = True
			cells.append(Cell(xx,yy,reachable)) #instancia a classe
	labirinto = Aestrela()

	labirinto.cells = cells
	labirinto.aberto = abertas

	cells[len(cells)-1] = end

	for i in range(len(cells)):
		print("("+str(cells[i].x)+","+str(cells[i].y)+"), "+str(cells[i].reachable))
	solvemaze(labirinto,start,end)
	
	#todas as celulas que sao cell.reachable == true
	# entram na lista de celulas abertas. self.aberto()

if __name__ == '__main__':
	main()
