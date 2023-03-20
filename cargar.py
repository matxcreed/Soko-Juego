import soko
import gamelib
import graficar
from pila import Pila
import pistas


def pila_de_estados(pila,tablero,nivel_estado_inicial): #se crea una pila con todos los estados desde el inicio del juego , para luego deshacerlo si lo desean 
	Pila.desapilar(pila)
	if Pila.ver_tope(pila) == nivel_estado_inicial:
		return nivel_estado_inicial
	else:
		tablero = Pila.desapilar(pila)
		return tablero

def dic_teclas():
	dic_tecla = {}
	with open("teclas.txt","r") as teclas:
		fin_archivo = True
		linea = teclas.readline()
		while fin_archivo:
			acciones = linea.split()
			if acciones != []:
				dic_tecla[acciones[0]] = acciones[2]
			linea = teclas.readline()
			if linea == "":
				fin_archivo = False

	return dic_tecla

def cargar_niveles(): #carga los niveles en un diccionario
	with open("niveles.txt","r") as fila_nivel:
		#nivel="Level " + nivel + "\n"
		tablero = []
		fin_nivel = True
		dic = {}
		i = 1
		while fin_nivel:
			nombre_nivel = fila_nivel.readline()
			fila_tablero = fila_nivel.readline()
			tablero = []
			if fila_tablero[0] == "'":
				fila_tablero = fila_nivel.readline()
			while fila_tablero  != "\n":
				fila = list(fila_tablero)
				if fila == []:
					break
				fila.pop(-1)
				tablero.append(fila)
				fila_tablero = fila_nivel.readline()
			i += 1
			dic[nombre_nivel] = tablero
			if fila_tablero == "" or nombre_nivel == "":
				fin_nivel = False
	return dic

def comandos(tablero,accion,estado_inicial,pila,pila_de_acciones):
	if accion == "NORTE":
		return soko.mover(tablero,(0,-1)),[]
	if accion == "ESTE":
		return soko.mover(tablero,(1, 0)),[]
	if accion == "OESTE":
		return soko.mover(tablero,(-1, 0)),[]
	if accion == "SUR":
		return soko.mover(tablero,(0, 1)),[]
	if accion == "REINICIAR":
		return estado_inicial,[]
	if accion == "SALIR":
		return 0
	if accion == "DESHACER":
		return pila_de_estados(pila,tablero,estado_inicial),[]
	if accion == "PISTAS":
		return pistas.crargar_o_desapilar_pila(tablero,pila_de_acciones)
		"""if Pila.esta_vacia(pila_de_acciones):
			pila_de_acciones = pistas.buscar_solucion(tablero,pila_de_acciones)
			return  tablero,pila_de_acciones
		direccion=Pila.desapilar(pila_de_acciones)
		tablero = soko.mover(tablero,(direccion[0],direccion[1]))
		return tablero,pila_de_acciones"""


"""def crargar_o_desapilar_pila(tablero,pila):
	if Pila.esta_vacia(pila):
		pila = pistas.buscar_solucion(tablero,pila)
		return  tablero,pila
	direccion = Pila.desapilar(pila)
	tablero = soko.mover(tablero,(direccion[0],direccion[1]))
	return tablero,pila
"""