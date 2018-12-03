import random
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
		(cx,cy,cd) = stack[-1]
		vizinhos_livres=[] #lista de vizinhos disponiveis
		for i in dirRange: #procurando nas 4 direcoes
			nx = cx+dx[i] ; ny = cy+dy[i] #nx e ny sao as coord do no candidato
			if nx >=0 and nx<size and ny>=0 and ny<size:
				if maze[ny][nx]==0: #se a celula estiver livre
				vizinhos_ocupados = 0 #numero de vizinhos ocupados deve ser 1
				for j in range(4):#procurando vizinhos nas 4 direcoes
					vizinho_x = nx+dx[j]; vizinho_y = ny+dy[j] #ex sao os vizinhos do no candidato
					if ex>=0 and ex<size and ey>=0 and ey<size:
						if maze[ey][ex] ==1: vizinhos_ocupados+=1
				if vizinhos_ocupados == 1: nlst.append(i)

		#se tiver um ou mais vizinhos livres, escolhe um aleatorio

		if len(nlst)>0:
			ir = nlst[random.randint(0,len(nlst)-1)]
			cx += dx[ir]; cy+=dy[ir]; maze[cy][cx]=1
			stack.append((cx,cy,ir))
		else:stack.pop()

		return maze
'''
se o maze eh caminho na posicao x,y, maze[y][x]==1
se o maze eh parede na posicao x,y, maze[y][x] == 0
'''


def solvemaze(maze, size):
	dx = [0,1,0,-1]; dy = [-1,0,1,0]
	color = [(0,0,0),(255,0,0)]
	cx =0 ; cy=0 #começando em 0,0
	stack = [(0,0,0)]
	steps= [[]]
	dirRange = range(4)
	nlst=[]
	for i in dirRange: #olhando ao redor
		look_x = cx+dx[i]; look_y = cy+dy[i]#testando se ta dentro do negocio
		if look_x >=0 and look_x < size and look_y >= 0 and look_y<size:
			if maze[look_y][look_x] == 1:
				nlst.append(i)
	if len(nlst)>0:
		ir = nlst[random.randint(0,len(nlst)-1)]
		cx += dx[ir]; cy += dy[ir];
		
	while len

while len(stack) > 0:






solution = list of steps taken
def metrics(solution):

def main():

if __name__ == '__main__':
	main()

