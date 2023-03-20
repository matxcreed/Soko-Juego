import soko
import graficar
import cargar
import gamelib
from pila import Pila 

def main():
    # Inicializar el estado del juego
    pila = Pila()
    accion = ""
    pila_de_acciones = Pila()
    gamelib.resize(500, 500)
    tablero,nivel_estado_inicial,pixeles_x,pixeles_y=graficar.inicio_sokoban()
    Teclas = cargar.dic_teclas()
    Pila.apilar(pila,tablero)
    while gamelib.is_alive():
        gamelib.draw_begin()
        graficar.graficar_fondo(pixeles_x*graficar.TAMANIO_CASILLA,pixeles_y*graficar.TAMANIO_CASILLA)
        graficar.graficar_nivel(tablero)
        if accion == "PISTAS":
            gamelib.draw_text("Pista lista",100,25)
        if soko.juego_ganado(tablero):
            gamelib.draw_image('img/ganador.gif', 0, 0)
            ev = gamelib.wait(gamelib.EventType.KeyPress)
            break
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key
        accion = Teclas[tecla]
        tablero,pila_de_acciones = cargar.comandos(tablero,accion,nivel_estado_inicial,pila,pila_de_acciones)
        Pila.apilar(pila,tablero)
        if tablero == 0:
            break
        # Actualizar el estado del juego, según la `tecla` presionada


gamelib.init(main)
