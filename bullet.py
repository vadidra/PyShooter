import pygame
from pygame import mixer
import os
import random
import csv
import button
from decoration import Decoration
from exit import Exit
from explosion import Explosion
from health_bar import HealthBar
from screen_fade import ScreenFade
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_TYPES, TILE_SIZE, BG, ROWS, COLS, GRAVITY, SCROLL_THRESH, BLACK, \
	RED, GREEN, PINK, FPS, WHITE, MAX_LEVELS
from water import Water


class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, direction, bullet_img, obstacle_list, screen_scroll,
				 player, bullet_group, enemy_group):
		pygame.sprite.Sprite.__init__(self)
		self.speed = 10
		self.image = bullet_img
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.direction = direction
		self.obstacle_list = obstacle_list
		self.screen_scroll = screen_scroll
		self.player = player
		self.bullet_group = bullet_group
		self.enemy_group = enemy_group

	def update(self):
		# move bullet
		self.rect.x += (self.direction * self.speed) + self.screen_scroll
		# check if bullet has gone off screen
		if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
			self.kill()
		# check for collision with level
		for tile in self.obstacle_list:
			if tile[1].colliderect(self.rect):
				self.kill()
		# check collision with characters
		if pygame.sprite.spritecollide(self.player, self.bullet_group, False):
			if self.player.alive:
				self.player.health -= 5
				self.kill()
		for enemy in self.enemy_group:
			if pygame.sprite.spritecollide(enemy, self.bullet_group, False):
				if enemy.alive:
					enemy.health -= 25
					self.kill()

