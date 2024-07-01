import pygame

from settings import TILE_SIZE


class Exit(pygame.sprite.Sprite):
	def __init__(self, img, x, y, screen_scroll):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))
		self.screen_scroll = screen_scroll
	def update(self):
		self.rect.x += self.screen_scroll

