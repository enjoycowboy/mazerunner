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

class Aestrela(object):
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

def busca_celulas_adjacentes(self,x,y):
	cells = []

	if cell.x < self.grid_width-1:
		cells.append(self.get_cell(cell.x+1, cell.y))
	if cell.y > 0:
		cells.append(self.get_cell(cell.x, cell.y-1))
	if cell.x > 0:
		cells.append(self.get_cell(cell.x-1, cell.y))
	if cell.y < self.grid_width-1:
		cells.append(self.get_cell(cell.x, cell.y+1))

		return cells

def path(self):
	cell = self.end
	while cell.parent is not self.start:
		cell = cell.parent
		maze[cell.y][cell.x]=3

def get_cell(self,x,y):
	 return self.cells[x * self.grid_height + y]

def get_path(self):
	cell = self.end
	path = [(cell.x, cell.y)]
	while cell.parent is not self.start:
		cell = cell.parent
		path.append((cell.x, cell.y))	
		path.append((self.start.x, self.start.y))
		path.reverse()
	return path

def atualiza_g_h(self, adjacente, cell):

	adjacente.g = cell.g + 10
	adjacente.h = self.calculo_h(adj)
	adjacente.pai = cell
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
	heapq.heappush(astar.aberto, (start.f, start))
	while len(aberto):
		# pop
		f, cell = heapq.heappop(aberto)
		fechado.add(cell)
		if cell is end:
			path()
			paint()
			break
		#captura adjacentes
		adj_cells = busca_celulas_adjacentes(cell)
		for adj_cell in adj_cells:
			if adj_cell.reachable and adj_cell not in fechado: # se nao estiver nos fechados
				if (adj_cell.f, adj_cell) in self.aberto: # confere se eh melhor do que antes
					if adj_cell.g > cell.g+10:
						atualiza_g_h(adj_cell, cell)
					else:
						atualiza_g_h(adj_cell, cell)
						heapq.heappush(self.aberto,(adj_cell.f,adj_cell))

def main():
	print("Lets RUN!")
	createmaze()

	astar = Aestrela()

	start = (0,0)
	end = (size-1,size-1)

	
	walls = []
	for xx in range(size):
		for yy in range(size):
			if maze[yy][xx] == 0:
				reachable = False
				walls.append((xx,yy))
			else: reachable = True
			astar.cells.append(Cell(x,y,reachable))
	
	solvemaze(astar,start,end)

if __name__ == '__main__':
	main()
