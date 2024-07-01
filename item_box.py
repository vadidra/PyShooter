import pygame
from pygame import mixer
import os
import random
import csv
import button
from bullet import Bullet
from decoration import Decoration
from exit import Exit
from explosion import Explosion
from grenade import Grenade
from health_bar import HealthBar
from screen_fade import ScreenFade
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_TYPES, TILE_SIZE, BG, ROWS, COLS, GRAVITY, SCROLL_THRESH, BLACK, \
	RED, GREEN, PINK, FPS, WHITE, MAX_LEVELS
from water import Water


class ItemBox(pygame.sprite.Sprite):
	def __init__(self, item_type, x, y, item_boxes, screen_scroll):
		pygame.sprite.Sprite.__init__(self)
		self.item_type = item_type
		self.image = item_boxes[self.item_type]
		self.rect = self.image.get_rect()
		self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))
		self.screen_scroll = screen_scroll
 
	def update(self, player):
		# scroll
		self.rect.x += self.screen_scroll
		# check if the player has picked up the box
		if pygame.sprite.collide_rect(self, player):
			# check what kind of box it was
			if self.item_type == 'Health':
				player.health += 25
				if player.health > player.max_health:
					player.health = player.max_health
			elif self.item_type == 'Ammo':
				player.ammo += 15
			elif self.item_type == 'Grenade':
				player.grenades += 3
			# delete the item box
			self.kill()

