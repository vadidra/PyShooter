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

class Grenade(pygame.sprite.Sprite):
	def __init__(self, x, y, direction, grenade_img, grenade_fx, obstacle_list, screen_scroll,
				 player, explosion_group, enemy_group):
		pygame.sprite.Sprite.__init__(self)
		self.timer = 100
		self.vel_y = -11
		self.speed = 7
		self.image = grenade_img
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.direction = direction
		self.grenade_fx = grenade_fx
		self.obstacle_list = obstacle_list
		self.screen_scroll = screen_scroll
		self.player = player
		self.explosion_group = explosion_group
		self.enemy_group = enemy_group

	def update(self):
		self.vel_y += GRAVITY
		dx = self.direction * self.speed
		dy = self.vel_y

		# check for collision with level
		for tile in self.obstacle_list:
			# check collision with walls
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				self.direction *= -1
				dx = self.direction * self.speed
			# check for collision in the y direction
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				self.speed = 0
				# check if below the ground, i.e. thrown up
				if self.vel_y < 0:
					self.vel_y = 0
					dy = tile[1].bottom - self.rect.top
				# check if above the ground, i.e. falling
				elif self.vel_y >= 0:
					self.vel_y = 0
					dy = tile[1].top - self.rect.bottom	

		# update grenade position
		self.rect.x += dx + self.screen_scroll
		self.rect.y += dy

		# countdown timer 
		self.timer -= 1
		if self.timer <= 0:
			self.kill()
			self.grenade_fx.play()
			explosion = Explosion(self.rect.x, self.rect.y, 0.5, self.screen_scroll)
			self.explosion_group.add(explosion)
			# do damage to anyone that is nearby
			if abs(self.rect.centerx - self.player.rect.centerx) < TILE_SIZE * 2 and \
				abs(self.rect.centery - self.player.rect.centery) < TILE_SIZE * 2:
				self.player.health -= 50
			for enemy in self.enemy_group:
				if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 2 and \
					abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 2:
					enemy.health -= 50


