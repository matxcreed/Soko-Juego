import gamelib
import soko
import cargar

TAMANIO_CASILLA=64

PARED = 'img/wall.gif'
PISO_IMG = 'img/ground.gif'
JUGADOR_IMG = 'img/player.gif'
CAJA_IMG = 'img/box.gif'
META_IMG = 'img/goal.gif'

TEXTO_NIVEL_X=250
TEXTO_NIVEL_y=425

TEXTO_NIVEL_INGRESADO_X=250
TEXTO_NIVEL_INGRESADO_Y=450

TEXTO_ENTER_X=250
TEXTO_ENTER_Y=475

def pantalla_incio():  #inicia las pantalla hasta la pantalla de elegir el nivel
    gamelib.draw_image('img/sokoban_pantalla1.gif', 0, 0)
    ev1 = gamelib.wait(gamelib.EventType.KeyPress)
    gamelib.draw_image('img/sokoban_niveles.gif', 0, 0)
    gamelib.draw_text("Ingrese el Numero de Nivel Deseado", TEXTO_NIVEL_X,TEXTO_NIVEL_y, fill = "yellow")

def elegir_nivel(): #elige el nivel deseado para jugar
    nivel = "Level "
    ev = gamelib.wait(gamelib.EventType.KeyPress)
    if ev.key in ("0","1","2","3","4","5","6","7","8","9"):
        ingreso_teclado = ev.key
    while True:

        nivel = nivel + ingreso_teclado
        gamelib.draw_begin()
        gamelib.draw_image('img/sokoban_niveles.gif', 0, 0)
        gamelib.draw_text("Ingrese el Numero de Nivel Deseado", TEXTO_NIVEL_X, TEXTO_NIVEL_y, fill = "yellow")
        gamelib.draw_text(nivel, TEXTO_NIVEL_INGRESADO_X, TEXTO_NIVEL_INGRESADO_Y, fill = "black", )
        gamelib.draw_text("Cuando termine ingrese ENTER", TEXTO_ENTER_X, TEXTO_ENTER_Y, fill = "yellow")
        gamelib.draw_end()
        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if ev.key == "BackSpace":
            lista_nivel = list(nivel)
            if lista_nivel[-1] == " ":
                continue
            nivel = nivel.replace(lista_nivel[-1],"")
            ingreso_teclado = ""
        else: 
            ingreso_teclado = ev.key


        if (ingreso_teclado == "Return"):
            break
    return nivel

def inicio_sokoban():
    gamelib.draw_begin()
    pantalla_incio()
    gamelib.draw_end()
    #ingreso_teclado = " "
    nivel = elegir_nivel()
    gamelib.title(nivel)
    nivel = nivel + "\n"
    dic_niveles = cargar.cargar_niveles()
    tablero = dic_niveles[nivel]
    nivel_estado_inicial = tablero
    pixeles_x, pixeles_y = (soko.dimensiones(tablero))
    gamelib.resize((pixeles_x * TAMANIO_CASILLA), (pixeles_y * TAMANIO_CASILLA))
    return tablero,nivel_estado_inicial,pixeles_x, pixeles_y

def graficar_fondo(largo,alto): #En el caso de que el nivel tenga lugares vacios , se llena con "PISO_IMG"
    y = 0
    x = 0
    while y <= alto:
        gamelib.draw_image(PISO_IMG, x, y)
        x += TAMANIO_CASILLA
        if x == largo:
            y += TAMANIO_CASILLA
            x = 0
    return 0

def graficar_nivel(tablero): # recorre el tablero para su graficacion
    y = 0
    for fila in tablero :
        x = 0
        for i in fila:
            graficar_caracter(i,x,y)
            x += TAMANIO_CASILLA
        y += TAMANIO_CASILLA
    return

def graficar_caracter(caracter,x,y):
    if caracter == soko.PARED:
        gamelib.draw_image(PISO_IMG, x, y)
        gamelib.draw_image(PARED, x, y)
    elif caracter == soko.JUGADOR:
        gamelib.draw_image(PISO_IMG, x, y)
        gamelib.draw_image(JUGADOR_IMG, x, y)
    elif caracter == soko.OBJETIVO:
        gamelib.draw_image(PISO_IMG, x, y)
        gamelib.draw_image(META_IMG, x, y)
    elif caracter == soko.LUGAR_LIBRE:
        gamelib.draw_image(PISO_IMG, x, y)
    elif caracter == soko.CAJA:
        gamelib.draw_image(PISO_IMG, x, y)
        gamelib.draw_image(CAJA_IMG, x, y)
    elif caracter == soko.CAJA_EN_OBJETIVO:
        gamelib.draw_image(PISO_IMG, x, y)
        gamelib.draw_image(CAJA_IMG, x, y)
        gamelib.draw_image(META_IMG, x, y)
    elif caracter == soko.JUGADOR_EN_OBJETIVO:
        gamelib.draw_image(PISO_IMG, x, y)
        gamelib.draw_image(META_IMG, x, y)
        gamelib.draw_image(JUGADOR_IMG, x, y)


    return



