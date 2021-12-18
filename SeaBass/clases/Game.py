from clases import conf, PlayableCharacter
from clases.conf import win_x, win_y, win_icon, velocidad
import pygame
pygame.font.init()
class Game:
    def __init__(self):
        # Atributos
        self.play = True
        self.setWinCaption("SeaBass")
        pygame.display.set_icon(win_icon)
        self.win = pygame.display.set_mode((win_x, win_y))
        self.pantalla = "inicio"
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        X = 400
        Y = 400
        font = pygame.font.Font('Arial', 32)
        text = font.render('GeeksForGeeks', True, green, blue)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 2)
    #Métodos
    def setPlay(self,boolean): #Cerrar aplicación
        self.play = boolean
    def setPantalla(self,pantalla): #Cambiar de pantalla (Inicio, outworld, pausa, pesca, etc)
        self.pantalla = pantalla
    def setWinCaption(self, texto): #Cambiar título de la ventana
        pygame.display.set_caption(texto)

    def crearTilemap(self):
        for i, row in enumerate(conf.TILEMAP):
            for j, column in enumerate(row):
                if column == 'P':
                    self.pc = PlayableCharacter.PC(j, i)
                elif column == 'B':
                    pass
                    # block.Block(j, i)

    def eventosOutworld(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.setPlay(self, False)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.pc.setterDir("izquierda")
                    self.pc.setterVectorX(-velocidad)
                if event.key == pygame.K_RIGHT:
                    self.pc.setterDir("derecha")
                    self.pc.setterVectorX(velocidad)
                if event.key == pygame.K_UP:
                    self.pc.setterVectorY(-velocidad)
                if event.key == pygame.K_DOWN:
                    self.pc.setterVectorY(velocidad)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.pc.setterVectorX(0)
                if event.key == event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.pc.setterVectorY(0)
            '''Otra forma
            teclas_pulsadas = pygame.key.get_pressed()
                if teclas_pulsadas[K_LEFT]:
                    print("Texto")
                    pc.setterX(32, "izquierda")'''
    def eventosInicio(self):
        self.display_surface.blit(self.text, self.textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.setPlay(self, False)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("enter")
                    self.setPantalla("outworld")

    def eventosPesca(self):
        pass