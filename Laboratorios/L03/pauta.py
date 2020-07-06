import random

####################
#### SOLUCIONES ####
####################

# Imports necesarios en solucion de problemas
import operator
from queue import PriorityQueue
import numpy as np

######## Problema 1a ########
def backtracking2(lentes, k, inicio, maximo):
  for i in range(len(lentes)-1, inicio-1, -1):
    if lentes[i] < maximo[i]:
      return
    elif lentes[i] > maximo[i]:
      maximo[:] = lentes[:]
      break
  if k == 0:
    return

  cambios = False
  for i in range(inicio-1,-1,-1):
    if lentes[inicio] <= lentes[i]: 
      lentes[inicio], lentes[i] = lentes[i], lentes[inicio]
      cambios = True
      backtracking2(lentes, k-1, inicio-1, maximo)
      lentes[inicio], lentes[i] = lentes[i], lentes[inicio]
  if not cambios:
    backtracking2(lentes, k, inicio-1, maximo)

def maximizar_amplificacion(lentes, k):
  final = lentes.copy()
  backtracking2(lentes.copy(), k, len(final)-1, final)
  return final
#############################

######## Problema 1b ######## RETORNA EL VALOR OPTIMO PARA ADMITIR VARIAS SOL
def seleccionar_vehiculos(vw, W):

	indexes = []

	T = [[0 for x in range(W + 1)] for y in range(len(vw) + 1)]

	for i in range(1, len(vw) + 1):
		for j in range(W + 1):

			if vw[i - 1][1] > j:
				T[i][j] = T[i - 1][j]
			else:
				indexes.append(i-1)
				T[i][j] = max(T[i - 1][j], T[i - 1][j - vw[i - 1][1]] + vw[i - 1][0])

	return T[len(vw)][W]
#############################

######## Problema 1c ########
def merge1c(A, aux, low, mid, high, count):

	k = i = low
	j = mid + 1
	c = 0

	while i <= mid and j <= high:

		if A[i] > A[j]:
			count[A[i]] = count.get(A[i], 0) + c
			aux[k] = A[i]
			i = i + 1
		else:
			aux[k] = A[j]
			j = j + 1
			c = c + 1

		k = k + 1

	while i <= mid:
		count[A[i]] = count.get(A[i], 0) + c
		aux[k] = A[i]
		k = k + 1
		i = i + 1

	for i in range(low, high + 1):
		A[i] = aux[i]


def mergeSort(A, aux, low, high, count):
	if high == low:
		return

	mid = low + ((high - low) >> 1)
	mergeSort(A, aux, low, mid, count)
	mergeSort(A, aux, mid + 1, high, count)
	merge1c(A, aux, low, mid, high, count)

def mas_adultos(cola_actual):
    count = {}
    cola = cola_actual.copy()
    aux = cola_actual.copy()
    cola_actual = cola_actual.copy()
    mergeSort(cola_actual, aux, 0, len(cola_actual) - 1, count)
    
    resp = []
    for i in cola:

        if not i in count:
            resp.append(0)
        else:
            resp.append(count[i])
    
    return resp
#############################

######## Problema 2a ########
import math 

class Point(): 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

def dist(p1, p2): 
	return math.sqrt((p1.x - p2.x) *
					(p1.x - p2.x) +
					(p1.y - p2.y) *
					(p1.y - p2.y)) 

def bruteForce(P, n): 
	min_val = float('inf') 
	for i in range(n): 
		for j in range(i + 1, n): 
			if dist(P[i], P[j]) < min_val: 
				min_val = dist(P[i], P[j]) 

	return min_val 

def stripClosest(strip, size, d): 
	min_val = d 
	strip.sort(key = lambda point: point.y) 

	for i in range(size): 
		j = i + 1
		while j < size and (strip[j].y -
							strip[i].y) < min_val: 
			min_val = dist(strip[i], strip[j]) 
			j += 1

	return min_val 

def closestUtil(P, n): 
	
	if n <= 3: 
		return bruteForce(P, n) 
  
	mid = n // 2
	midPoint = P[mid] 

	dl = closestUtil(P[:mid], mid) 
	dr = closestUtil(P[mid:], n - mid) 

	d = min(dl, dr) 

	strip = [] 
	for i in range(n): 
		if abs(P[i].x - midPoint.x) < d: 
			strip.append(P[i]) 

	return min(d, stripClosest(strip, len(strip), d)) 

def closest(P, n): 
	P.sort(key = lambda point: point.x) 

	return closestUtil(P, n) 
 
def codigo_6d2(planes):
    P = []
    for p in planes:
        P.append(Point(p[0], p[1]))
    n = len(P)
    return closest(P, n)
#############################

######## Problema 2b #########
def is_valid(result, new_height):
    return not result or result[-1][1] != new_height

def merge(left, right):
    h1, h2 = 0, 0
    i, j = 0, 0
    result = []
    
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            h1 = left[i][1]
            corner = left[i][0]
            i += 1
        elif right[j][0] < left[i][0]:
            h2 = right[j][1]
            corner = right[j][0]
            j += 1
        else:
            h1 = left[i][1]
            h2 = right[j][1]
            corner = right[j][0]
            i += 1
            j += 1

        if is_valid(result, max(h1, h2)):
            result.append((corner, max(h1, h2)))

    result.extend(right[j:])
    result.extend(left[i:])
    return result

def prefil_de_muro(bloques):
    if not bloques:
        return []
    if len(bloques) == 1:
        return [[bloques[0][0], bloques[0][1]], [bloques[0][2], 0]]

    mid = len(bloques) // 2
    left = prefil_de_muro(bloques[:mid])
    right = prefil_de_muro(bloques[mid:])
    return merge(left, right)
#############################

######## Problema 3a #########
class GameState():
    def __init__(self, state, goal_state, level, parent = None, heuristic_func = "manhattan"):
        self.__state = state
        self.__goal_state = goal_state
        self.__level = level
        self.__heuristic_func = heuristic_func
        self.__heuristic_score = level
        self.__parent = parent
        self.calculate_fitness()
        
    def __hash__(self):
        return hash(str(self.__state))
        
    def __lt__(self, other):
        return self.__heuristic_score < other.__heuristic_score
    
    def __eq__(self, other):
        return self.__heuristic_score == other.__heuristic_score
    
    def __gt__(self, other):
        return self.__heuristic_score > other.__heuristic_score
    
    def get_state(self):
        return self.__state
    
    def get_score(self):
        return self.__heuristic_score
    
    def get_level(self):
        return self.__level
    
    def get_parent(self):
        return self.__parent
    
    def calculate_fitness(self):
        if self.__heuristic_func == "misplaced_tiles":
            for cur_tile, goal_tile in zip(self.__state, self.__goal_state):
                if cur_tile != goal_tile:
                    self.__heuristic_score += 1
        elif self.__heuristic_func == "manhattan":
            for cur_tile in self.__state:
                cur_idx = self.__state.index(cur_tile)
                goal_idx = self.__goal_state.index(cur_tile)
                cur_i, cur_j = cur_idx // int(np.sqrt(len(self.__state))), cur_idx % int(np.sqrt(len(self.__state)))
                goal_i, goal_j = goal_idx // int(np.sqrt(len(self.__state))), goal_idx % int(np.sqrt(len(self.__state)))
                self.__heuristic_score += self.calculate_manhattan(cur_i, cur_j, goal_i, goal_j)
        else:
            print('Unknown heuristic function is being used.')
            
    def calculate_manhattan(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

class Solver():
    def __init__(self, init_state, goal_state, heuristic_func = "manhattan", max_iter = 10000):
        self.__init_state = init_state
        self.__goal_state = goal_state
        self.__heuristic_func = heuristic_func
        self.__MAX = 100000
        self.__max_iter = max_iter
        self.__path = []
        
    def solve(self):
        x_axis = [1, 0, -1,  0]
        y_axis = [0, 1,  0, -1]
        
        level = 0
        visited_nodes = set()
               
        nodes = PriorityQueue(self.__MAX)
        init_node = GameState(self.__init_state.flatten().tolist(), self.__goal_state.flatten().tolist(), level, parent = None, heuristic_func = self.__heuristic_func)
        nodes.put(init_node)
        
        epochs = 0
        while nodes.qsize() and epochs <= self.__max_iter:
            epochs += 1
            
            cur_node = nodes.get()
            cur_state = cur_node.get_state()
            
            if str(cur_state) in visited_nodes:
                continue
            visited_nodes.add(str(cur_state))
            
            if cur_state == self.__goal_state.flatten().tolist():
                while cur_node.get_parent():
                    self.__path.append(cur_node)
                    cur_node = cur_node.get_parent()
                break
            
            empty_tile = cur_state.index(0)
            i, j = empty_tile // self.__goal_state.shape[0], empty_tile % self.__goal_state.shape[0]
            
            cur_state = np.array(cur_state).reshape(self.__goal_state.shape[0], self.__goal_state.shape[0])
            for x, y in zip(x_axis, y_axis):
                new_state = np.array(cur_state)
                if i + x >= 0 and i + x < self.__goal_state.shape[0] and j + y >= 0 and j + y < self.__goal_state.shape[0]:
                    new_state[i, j], new_state[i+x, j+y] = new_state[i+x, j+y], new_state[i, j]
                    game_state = GameState(new_state.flatten().tolist(), self.__goal_state.flatten().tolist(), cur_node.get_level() + 1, cur_node, self.__heuristic_func)
                    if str(game_state.get_state()) not in visited_nodes:
                        nodes.put(game_state)
        if epochs > self.__max_iter:
            print('This grid setting is not solvable')
        return self.__path
        
def reorganizar_habitacion(estado_inicial, estado_final):
    init_state = np.array([[0 if j == '_' else int(j) for j in row] for row in estado_inicial])
    goal_state = np.array([[0 if j == '_' else int(j) for j in row] for row in estado_final])
    path = Solver(init_state, goal_state).solve()
    return len(path)

#############################

######## Problema 3b #########
class Predio(): 
  
    def __init__(self, retazos, caminos): 
        self.V = retazos
        self.graph = None

        self.graph = []
        for i in range(retazos):
            l = [0]*retazos
            self.graph.append(l)
        
        for i in range(len(caminos)):
            ori = caminos[i][0]
            dest = caminos[i][1]
            self.graph[ori][dest] = 1
            self.graph[dest][ori] = 1
  
    def isSafe(self, v, arr, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and arr[i] == c: 
                return False
        return True
       
    def graphArrendatarioUtil(self, m, arr, v): 
        if v == self.V: 
            return True
  
        for c in range(1, m+1): 
            if self.isSafe(v, arr, c) == True: 
                arr[v] = c 
                if self.graphArrendatarioUtil(m, arr, v+1) == True: 
                    return True
                arr[v] = 0
  
    def graphArrendatario(self, m): 
        arr = [0] * self.V 
        if self.graphArrendatarioUtil(m, arr, 0) == None: 
            return (False, None)
  
        return (True, arr)
   
def minimos_arrendatarios(retazos, caminos):
    new_caminos = []
    for c in caminos:
        new_caminos.append((c[0]-1,c[1]-1))
    g = Predio(retazos, new_caminos)
    for nColors in range(1,retazos+1):
        ver = g.graphArrendatario(nColors)
        if g.graphArrendatario(nColors)[0]:
            arr = ver[1]
            max_arr = max(arr)
            resp = [[] for _ in range(max_arr)]
            for i, t in enumerate(arr):
                resp[t-1].append(i+1)
            return resp
#############################

################
#### INPUTS ####
################

def inputs_p1a(size, seed):
    random.seed(seed)
    lentes = [int(random.uniform(1,min((10000,size))+1)) for _ in range(size)]
    k = random.randint(1,4)
    return [lentes, k]

def inputs_p1b(size, seed):
    random.seed(seed)
    valores_y_tiempos = []
    for _ in range(size):
        v = random.randint(1,min(size, 1000))
        t = random.randint(1,min(size, 100))
        valores_y_tiempos.append((v,t))
    tiempo_total_maximo = random.randint(size, 3*size)
    return [valores_y_tiempos, tiempo_total_maximo]

def inputs_p1c(size, seed):
    random.seed(seed)
    cola_actual = []
    while len(cola_actual) < size:
        v = int(random.uniform(1,min((10000,size*2))+1))
        if not v in cola_actual:
            cola_actual.append(v)
    return [cola_actual]

def inputs_p2a(size, seed):
    random.seed(seed)
    points = []
    for _ in range(size):
        x = random.randint(max(-100000, -size), min(size, 100000))
        y = random.randint(max(-100000, -size), min(size, 100000))
        points.append((x,y))
    return [points]

def inputs_p2b(size, seed):
    random.seed(seed)
    muro = []
    for _ in range(size):
        a = random.randint(0, size)
        b = a + random.randint(1, size*2)
        h = random.randint(1, 100)
        muro.append((a,h,b))
    return [muro]

def solvable(tiles):
    count = 0

    for i in range(8):
        for j in range(i+1, 9):
            if tiles[j] and tiles[i] and tiles[i] > tiles[j]:
                count += 1

    return count % 2 == 0

def inputs_p3a(size, seed):
    random.seed(seed)
    while True:
        initial = [1,2,3,4,5,6,7,8,0]
        random.shuffle(initial)
        pos = initial.index(0)
        if solvable(initial):
            initial[pos] = '_'
            return [[initial[0:3], initial[3:6], initial[6:9]], [[1,2,3],[4,5,6],[7,8,'_']]]

def inputs_p3b(size, seed):
    random.seed(seed)
    caminos = []
    len_caminos = size
    while len(caminos) < len_caminos:
        x = random.randint(1,size)
        y = random.randint(1,size)

        if x!=y and not (((x,y) in caminos) or ((y,x) in caminos)):
            caminos.append((x,y))
    return [size, caminos]
    
#######################
#### VERIFICADORES ####
#######################

def verificar_p1a(resp, inputs):
    correcta = maximizar_amplificacion(*inputs)
    if resp == correcta:
        return 1
    else:
        return 0

def verificar_p1b(resp, inputs):
    valor_optimo = seleccionar_vehiculos(*inputs)
    valor_t = 0
    tiempo_t = 0

    for i in resp:
        valor_t += inputs[0][i][0]
        tiempo_t += inputs[0][i][1]

    if valor_t == valor_optimo and tiempo_t <= inputs[1]:
        return 1
    else:
        return 0

def verificar_p1c(resp, inputs):
    correcta = mas_adultos(*inputs)
    if resp == correcta:
        return 1
    else:
        return 0

def distrev(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))


def verificar_p2a(resp, inputs):
    dist_lin = codigo_6d2(*inputs)
    dAlumn = distrev(resp[0], resp[1])
    if dist_lin == dAlumn:
        return 1
    else:
        return 0

def verificar_p2b(resp, inputs):
    correcta = prefil_de_muro(*inputs)
    correcta[-1] = tuple(correcta[-1])
    if str(resp) == str(correcta):
        return 1
    else:
        return 0

def verificar_p3a(resp, inputs):
    correcta = reorganizar_habitacion(*inputs)
    if resp == correcta:
        return 1
    else:
        return 0

def verificar_p3b(resp, inputs):
    correcta = minimos_arrendatarios(*inputs)
    n_arrendatarios = len(correcta)

    ver = 0
    for c in inputs[1]:
        for t in resp:
            if c[0] in t and c[1] in t:
                ver += 1
                break    

    if len(resp) == n_arrendatarios and ver == 0:
        return 1
    else:
        return 0
