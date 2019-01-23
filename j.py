#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame
import time
from pygame.locals import *
 
pygame.init()
# print(pygame.font.get_fonts())

#my_font = pygame.font.SysFont("cambria", 46)
my_font = pygame.font.Font("myfont.ttf", 46)
text_surface = my_font.render(u"高度", True, (25,150,50), (0,255,255))
my_font = pygame.font.Font("myfont.ttf", 46)
text_surface2 = my_font.render(u"建", True, (25,150,50))
# textpos = text_surface2.get_rect(center=(300,100))
textpos = (0, 100)
print text_surface.get_width(), text_surface.get_height()
print type(my_font)

text_surface2 = pygame.transform.smoothscale(text_surface2, (196, 68))
print 	type(text_surface)
# 2.创建游戏窗口
# set_mode((宽度， 高度))
screen = pygame.display.set_mode((600, 400),RESIZABLE,32)



# 3.游戏循环
while True:
	# 检测事件
	for event in pygame.event.get():
		# 检测窗口上的关闭按钮是否被点击
		if event.type == pygame.QUIT:
			# 退出游戏
			print('关闭按钮被点击')
			exit()
	screen.fill((255,255,255))
	screen.blit(text_surface2,textpos)
	# rect = pygame.draw.rect(screen, (0, 255, 0), ((200, 5), (200, 200)), 0)
	# screen.blit(text_surface, (0, 0))
	text_surface.blit(screen, (0, 0))
	
	# print type(rect)

	pygame.display.update()

	time.sleep(0.1)
