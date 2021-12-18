#Imports
import pygame
from clases import PlayableCharacter, Game, conf, block

#Creación de elementos
game = Game.Game()
game.crearTilemap()

#Metodos
pygame.init()

#GameLoop
if __name__ == '__main__':
    while game.play:

        #Actualizaciones
        if game.pantalla == "inicio":
            game.eventosInicio()
            game.win.fill((30, 30, 30))

        elif game.pantalla == "outworld":
            game.eventosOutworld()
            game.win.fill((255, 255, 255))
            #pc.blitPC(game.win)

        elif game.pantalla == "pesca":
            game.eventosPesca()

        #Dibujado
        pygame.display.update()
        pygame.time.Clock().tick(60)

    #Salida del bucle
    print("Finalizando ejecución")