import pygame
from clases.conf import tilesize, pc_image

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.game = pygame.sprite.LayeredUpdates()
        self._layer = 2
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        self.image = pc_image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y