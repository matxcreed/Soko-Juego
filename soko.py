CAJA="$"
CAJA_EN_OBJETIVO="*"
JUGADOR="@"
JUGADOR_EN_OBJETIVO="+"
PARED="#"
OBJETIVO="."   
LUGAR_LIBRE=" " 

def crear_grilla(desc):             #Crea una grilla a partir de la descripción del estado inicial.
    grilla = []						#La descripción es una lista de cadenas, cada cadena representa una
    for i in desc:					#fila y cada caracter una celda. Los caracteres pueden ser los siguientes:
        fila = list(i)
        grilla.append(fila)			#Caracter  Contenido de la celda
    return grilla 					#--------  ---------------------
									#   #  Pared
    								#	$  Caja
           							#	@  Jugador
           							#	.  Objetivo
           							#	*  Objetivo + Caja
           							#	+  Objetivo + Jugador

    								#	Ejemplo:

    								#	>>> crear_grilla([
        							#	'#####',
        							#	'#.$ #',
        							#	'#@  #',
        							#	'#####',
    								#	])
									


def dimensiones(grilla): #Devuelve una tupla con la cantidad de columnas y filas de la grilla.

    fila_max = 0
    columna_max = 0
    for fila in grilla:
        columna_max += 1
        if fila_max <= len(fila):
            fila_max = len(fila)
    return (fila_max,columna_max)


def hay_pared(grilla,c,f): #Devuelve True si hay una pared en la columna y fila (c, f).
    return PARED == grilla[f][c]

def hay_objetivo(grilla,c,f): #Devuelve True si hay un objetivo en la columna y fila (c, f).
    return OBJETIVO == grilla[f][c] or JUGADOR_EN_OBJETIVO == grilla[f][c] or CAJA_EN_OBJETIVO == grilla[f][c]

def hay_caja(grilla,c,f): #Devuelve True si hay una caja en la columna y fila (c, f).
    return CAJA == grilla[f][c] or CAJA_EN_OBJETIVO == grilla[f][c]

def hay_jugador(grilla,c,f): #Devuelve True si el jugador está en la columna y fila (c, f).
    return JUGADOR == grilla[f][c] or JUGADOR_EN_OBJETIVO == grilla[f][c]

def juego_ganado(grilla): #Devuelve True si el juego está ganado.
    fila_clear = 0
    for i in grilla:
        if ((JUGADOR_EN_OBJETIVO not in i) and (OBJETIVO not in i) and (CAJA not in i) and (PARED in i)):
            if (CAJA_EN_OBJETIVO in i):
                ganaste = True
        else:
            return False
    return ganaste

def posicion_jugador(grilla):#devuelve la posicion del jugador
    for fila_jugador in range (len(grilla)):
        for columna_jugador  in range (len(grilla[fila_jugador])):
            if grilla[fila_jugador][columna_jugador] == JUGADOR or grilla[fila_jugador][columna_jugador] == JUGADOR_EN_OBJETIVO:
                return fila_jugador,columna_jugador


def mover(grilla,direccion): #Mueve el jugador en la dirección indicada
    fila_jugador,columna_jugador = posicion_jugador(grilla)
    fila_direccion = direccion[1]
    columna_direccion = direccion[0]
    mov = movimiento_posible(grilla,columna_direccion,fila_direccion,fila_jugador,columna_jugador)
    if (mov[1] == LUGAR_LIBRE):
        caracter = grilla[fila_jugador][columna_jugador]
        grilla_n = siguiente_casilla(fila_jugador,columna_jugador, fila_direccion,columna_direccion,grilla,caracter,mov)
        return  grilla_n
    elif  (mov[1] == OBJETIVO):
        caracter = grilla[fila_jugador][columna_jugador]
        grilla_n = siguiente_casilla(fila_jugador,columna_jugador,fila_direccion,columna_direccion,grilla,caracter,mov)
        return grilla_n
    elif (grilla[fila_jugador + fila_direccion][columna_jugador + columna_direccion] == CAJA) or (grilla[fila_jugador + fila_direccion][columna_jugador + columna_direccion] == CAJA_EN_OBJETIVO):
        mov = movimiento_posible(grilla,(2*columna_direccion),(2*(direccion)[1]),fila_jugador,columna_jugador)
        caracter=grilla[fila_jugador + fila_direccion][columna_jugador + columna_direccion]
        fila_jugador_desplazado = (fila_jugador + fila_direccion)
        columna_jugador_desplazado = (columna_jugador + columna_direccion)
        fila_siguiente_movimiento = (fila_jugador + (2*fila_direccion))
        columna_siguiente_movimiento = (columna_jugador + (2*columna_direccion))
        if mov[1] == LUGAR_LIBRE:
            grilla_caja_ubicada = siguiente_casilla(fila_jugador_desplazado,columna_jugador_desplazado,fila_siguiente_movimiento,columna_siguiente_movimiento,grilla,caracter,mov)
            #grilla_caja_ubicada = nueva_grilla(fila_jugador_desplazado, columna_jugador_desplazado, fila_siguiente_movimiento, columna_siguiente_movimiento, grilla, CAJA, LUGAR_LIBRE)
            caracter=grilla[fila_jugador][columna_jugador]
            mov = movimiento_posible(grilla_caja_ubicada, columna_direccion, fila_direccion, fila_jugador, columna_jugador)
            grilla_n = siguiente_casilla(fila_jugador,columna_jugador,fila_direccion,columna_direccion, grilla_caja_ubicada,caracter,mov)
            return grilla_n
        elif mov[0]:
            grilla_caja_ubicada = siguiente_casilla(fila_jugador_desplazado, columna_jugador_desplazado, fila_siguiente_movimiento, columna_siguiente_movimiento, grilla,caracter,mov)
            caracter = grilla[fila_jugador][columna_jugador]
            mov = movimiento_posible(grilla_caja_ubicada, columna_direccion, fila_direccion, fila_jugador, columna_jugador)
            grilla_n = siguiente_casilla(fila_jugador,columna_jugador,fila_direccion,columna_direccion, grilla_caja_ubicada,caracter,mov)
            return grilla_n
    return grilla



def siguiente_casilla(fila_objeto,columna_objeto,fila_direccion,columna_direccion,grilla,caracter,mov): #en el caso de que muevas una caja , esta funcion luego de mover la caja mueve al jugador
    #mov = movimiento_posible(grilla,columna_direccion,fila_direccion,fila_objeto,columna_objeto)
    if ( mov[1] == LUGAR_LIBRE) :#fila_objeto fila
        if caracter == JUGADOR_EN_OBJETIVO:
            return nueva_grilla(fila_objeto,columna_objeto,(fila_objeto + fila_direccion),(columna_objeto + columna_direccion) ,grilla,JUGADOR ,OBJETIVO)
        elif caracter == JUGADOR:
            return nueva_grilla(fila_objeto, columna_objeto, (fila_objeto + fila_direccion),(columna_objeto + columna_direccion), grilla, JUGADOR, LUGAR_LIBRE)
        elif caracter == CAJA:
           return nueva_grilla(fila_objeto, columna_objeto, fila_direccion, columna_direccion, grilla, CAJA,LUGAR_LIBRE)
        elif caracter == CAJA_EN_OBJETIVO:
            return nueva_grilla(fila_objeto, columna_objeto, fila_direccion, columna_direccion, grilla, CAJA,OBJETIVO)
    elif  (mov[1] == OBJETIVO):
        if caracter == JUGADOR:
            return nueva_grilla(fila_objeto, columna_objeto, (fila_objeto + fila_direccion),(columna_objeto + columna_direccion), grilla, JUGADOR_EN_OBJETIVO, LUGAR_LIBRE)
        elif caracter == JUGADOR_EN_OBJETIVO:
            return nueva_grilla(fila_objeto, columna_objeto, (fila_objeto + fila_direccion),(columna_objeto + columna_direccion), grilla, JUGADOR_EN_OBJETIVO, OBJETIVO)
        elif caracter == CAJA_EN_OBJETIVO:
            return nueva_grilla(fila_objeto, columna_objeto,  fila_direccion, columna_direccion, grilla, CAJA_EN_OBJETIVO, OBJETIVO)
        else:
            return nueva_grilla(fila_objeto, columna_objeto,  fila_direccion, columna_direccion, grilla, CAJA_EN_OBJETIVO, LUGAR_LIBRE)



def movimiento_posible(grilla,columna_direccion,fila_direccion,fila_objeto,columna_objeto): #chequea si el movimiento en la direccion indiacada es valido
    if (grilla[fila_objeto +fila_direccion ][columna_objeto + columna_direccion] == LUGAR_LIBRE) or (grilla[fila_objeto + fila_direccion][columna_objeto + columna_direccion] == OBJETIVO):
        return (True,grilla[fila_objeto + fila_direccion][columna_objeto + columna_direccion])
    else:
        return (False,False)


def nueva_grilla(fila_objeto,columna_objeto,fila_destino,columna_destino,grilla,caracter_en_movimiento,caracter_a_reemplazar):#caracter_en_movimiento caracter que se mueve, caracter_a_reemplazar caracter a reemplazar
    grilla_n = []
    for  i in range (len(grilla)):
        if i == fila_destino and i == fila_objeto:
            fila = mod_fila(grilla[i],columna_destino,caracter_en_movimiento)
            fila = mod_fila(fila,columna_objeto,caracter_a_reemplazar)
            grilla_n.append(fila)
        elif i == fila_destino:
            fila = mod_fila(grilla[i], columna_destino, caracter_en_movimiento)
            grilla_n.append(fila)
        elif i == fila_objeto:
            fila = mod_fila(grilla[i],columna_destino,caracter_a_reemplazar)
            grilla_n.append(fila)
        else:
            grilla_n.append(grilla[i])
    return grilla_n

def mod_fila(fila_modificada,columna_modificada,caracter_sustituto): #copia la fila original , para luego actualiar la fila copiada con el movimiento realizado    
    fila_nueva_modificada = []
    fila_nueva_modificada.extend(fila_modificada)
    fila_nueva_modificada[columna_modificada] = caracter_sustituto
    return fila_nueva_modificada





