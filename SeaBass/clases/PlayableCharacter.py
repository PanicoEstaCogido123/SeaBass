from clases.conf import tilesize, pc_image, default_dir
import pygame


class PC:
    def __init__(self, tilemap_x, tilemap_y):
        # Atributos
        self.image = pc_image
        self.x=tilemap_x*tilesize
        self.y=tilemap_y*tilesize
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.vectorX=0
        self.vectorY=0
        self.pc_dir=default_dir
        # Statement de creación (para pruebas)
        print("Soy un "+ str(self.__class__.__name__)+ " ,mis cordenadas son "+ str(self.x)+" "+ str(self.y)+ " y estoy mirando a la "+str(self.pc_dir))

    #Métodos
    def setterDir(self, direccion):
        self.pc_dir=direccion

    def setterVectorX(self, vector):
        self.vectorX=vector

    def setterVectorY(self, vector):
        self.vectorY=vector

    def blitPC(self,window):
        self.x += self.vectorX
        self.y += self.vectorY
        if self.pc_dir == "derecha":
            window.blit(self.image, (self.x, self.y))
        else:
            window.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))