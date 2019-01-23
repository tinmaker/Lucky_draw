#coding=utf-8
'''
Created on 2017年2月27日
@author: zxt
'''
import pygame
from pygame.locals import RESIZABLE, QUIT, VIDEORESIZE
from sys import exit
 
background_image_filename = './image/locky_bg1.jpg'
 
SCREEN_SIZE = (640, 480)
 
pygame.init()
# 标志位RESIZABLE    创建一个可以改变大小的窗口
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
pygame.display.set_caption("Window resized to " + str(SCREEN_SIZE))
 
background2 = background = pygame.image.load(background_image_filename).convert()
# background = pygame.transform.smoothscale(background, (1855, 1056))
print type(background)
screen.blit(background2, (0, 100))

my_font = pygame.font.Font("myfont.ttf", 46)
text_surface = my_font.render(u"高度", True, (25,150,50), (0,255,255))
# background.blit(background2, (100, -100))
# pygame.display.update()
while True:
    
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen == pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to " + str(event.size))
    
        # background2 = pygame.transform.smoothscale(background, SCREEN_SIZE)
        print SCREEN_SIZE
        # screen.blit(background, (0, 0))
        # pygame.display.update()
    screen_width, screen_height = SCREEN_SIZE
    # 这里需要重新填充满窗口
    # for y in range(0, screen_height, background.get_height()):
    #     for x in range(0, screen_width, background.get_width()):
    screen.blit(background2, (0, 100))
    screen.blit(text_surface, (0, 90))
    pygame.draw.rect(screen,[255,0,0],[100,100,100,100],0)
    # screen.blit(background2, (0, 0))
    # background.blit(background2, (100, -100))
    
    pygame.display.update()