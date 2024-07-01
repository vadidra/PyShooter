import pygame
from pygame import mixer
import os
import random
import csv
import button

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.5)

# Create a display surface object of specific dimension
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PyShooter - WIP')

# Creating a new clock object to track the amount of time
# clock = pygame.time.Clock()
# FPS (Frames Per Second): Frame rate is the measurement of how quickly a number of frames appears within a second. 
# frequency at which consecutive images are captured or displayed.
# set framerate
FPS = 60

# define game variables
GRAVITY = 0.75
SCROLL_THRESH = 200
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
MAX_LEVELS = 3
# screen_scroll = 0
# bg_scroll = 0
# level = 1
# start_game = False
# start_intro = False
#
#
# # define player action variables
# moving_left = False
# moving_right = False
# shoot = False
# grenade = False
# grenade_thrown = False

# # load music and sounds
# pygame.mixer.music.load('audio/music2.mp3')
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.play(-1, 0.0, 5000)  # (loops, start, fade_ms) # loop = -1 => infinite loop; start = 0.0 => time from which the music starts playing; fade_ms is an optional integer argument, which is 0 by default, which denotes the period of time (in milliseconds) over which the music will fade up from volume level 0.0 to full volume
# jump_fx = pygame.mixer.Sound('audio/jump.wav')
# jump_fx.set_volume(0.05)
# shot_fx = pygame.mixer.Sound('audio/shot.wav')
# shot_fx.set_volume(0.05)
# grenade_fx = pygame.mixer.Sound('audio/grenade.wav')
# grenade_fx.set_volume(0.05)

# load images
# button images
# # pygame.image.load() function call will return a Surface object that has the image drawn on it.
# # convert() and convert_alpha() are both used to convert surfaces to the same pixel format as used by the screen.
# start_img = pygame.image.load('img/start_btn.png').convert_alpha()
# exit_img = pygame.image.load('img/exit_btn.png').convert_alpha()
# restart_img = pygame.image.load('img/restart_btn.png').convert_alpha()
# # background
# pine1_img = pygame.image.load('img/background/pine1.png').convert_alpha()
# pine2_img = pygame.image.load('img/background/pine2.png').convert_alpha()
# mountain_img = pygame.image.load('img/background/mountain.png').convert_alpha()
# sky_img = pygame.image.load('img/background/sky_cloud.png').convert_alpha()
# # store tiles in a list
# img_list = []
# for x in range(TILE_TYPES):
# 	img = pygame.image.load(f'img/tile/{x}.png')
# 	# To scale the image we use the pygame.transform.scale()
# 	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
# 	img_list.append(img)
# # bullet
# bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()
# # grenade
# grenade_img = pygame.image.load('img/icons/grenade.png').convert_alpha()
# # pick up boxes
# health_box_img = pygame.image.load('img/icons/health_box.png').convert_alpha()
# ammo_box_img = pygame.image.load('img/icons/ammo_box.png').convert_alpha()
# grenade_box_img = pygame.image.load('img/icons/grenade_box.png').convert_alpha()
# item_boxes = {
# 	'Health'	: health_box_img,
# 	'Ammo'		: ammo_box_img,
# 	'Grenade'	: grenade_box_img
# }

# define colours
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)

# define font
# font = pygame.font.SysFont('Futura', 30)


# # create screen fades
# # create buttons
# start_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 150, start_img, 1)
# exit_button = button.Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 50, exit_img, 1)
# restart_button = button.Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, restart_img, 2)
#
# # create sprite groups
# enemy_group = pygame.sprite.Group()
# bullet_group = pygame.sprite.Group()
# grenade_group = pygame.sprite.Group()
# explosion_group = pygame.sprite.Group()
# item_box_group = pygame.sprite.Group()
# decoration_group = pygame.sprite.Group()
# water_group = pygame.sprite.Group()
# exit_group = pygame.sprite.Group()
# # create empty tile list
# world_data = []
# for row in range(ROWS):
# 	r = [-1] * COLS
# 	world_data.append(r)
# # load in level data and create world
# with open(f'level{level}_data.csv', newline='') as csvfile:
# 	reader = csv.reader(csvfile, delimiter=',')
# 	for x, row in enumerate(reader):
# 		for y, tile in enumerate(row):
# 			world_data[x][y] = int(tile)



