import random
import pygame

win_width = 1000
win_height = 800
font_px = 15

pygame.init()
winsur = pygame.display.set_mode((win_width, win_height))
font = pygame.font.SysFont("consolas", font_px)
bg_surface = 