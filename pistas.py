import soko
from pila import Pila

def convertir_tablero_en_tuplas(tablero): # convierte el tablero (una lista de listas) en una tupla de tuplas para que sea inmutable y pueda usarse para el diccionario
	tablero_inmutable=[]
	for linea in tablero:
		fila=tuple(linea)
		tablero_inmutable.append(fila)
	return tuple(tablero_inmutable)

def buscar_solucion(estado_incial,pila_de_acciones):
	visitados={}
	solucion,acciones = backtrack(estado_incial,visitados)
	pila_de_acciones = pilas_acciones(acciones,pila_de_acciones)
	return pila_de_acciones

def backtrack(estado,visitados):
	estado_convertido = convertir_tablero_en_tuplas(estado)
	visitados[estado_convertido] = True
	direcciones = [[0,1],[0,-1],[1,0],[-1,0]]
	if soko.juego_ganado(estado):
	# ¡encontramos la solución!p
		return True,[]
	for direccion in direcciones:
		nuevo_estado = soko.mover(estado,direccion)
		accion = direccion
		if convertir_tablero_en_tuplas(nuevo_estado) in visitados:
			continue
		solucion_encontrada,acciones = backtrack(convertir_tablero_en_tuplas(nuevo_estado),visitados)
		if solucion_encontrada:
			acciones = acciones + accion
			return True,acciones
	return False,0


def pilas_acciones(acciones,pila):#pasa la lista de acciones que devuelve el backtrack a una pila de acciones
	for direccion_1, direccion_2  in zip(acciones[0::2],acciones[1::2]):
		direccion = [direccion_1,direccion_2]
		Pila.apilar(pila,direccion)
	return pila

def crargar_o_desapilar_pila(tablero,pila):#si la pila esta vacia , la carga con las acciones para solucionar el nivel , si no desapila la accion y realiza dicha accion
	if Pila.esta_vacia(pila):
		pila = buscar_solucion(tablero,pila)
		return  tablero,pila
	direccion = Pila.desapilar(pila)
	tablero = soko.mover(tablero,(direccion[0],direccion[1]))
	return tablero,pila

