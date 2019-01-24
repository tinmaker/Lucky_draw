#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from rollLockydraw import *
import time
import datetime

pygame.init()

namelists = [u"小洪", u"小明", u"小花", u"小华", u"韩梅梅", u"李雷", u"小李"]
pygame.init()
ttf = "myfont.ttf"
bg2 = bg=pygame.image.load('./image/locky_bg1.jpg')
x = 0
y = 40
count =0
max_x = 2
bg_size = bg.get_size()
screen = pygame.display.set_mode(bg_size,RESIZABLE,32)
roll = RollLockydraw(namelists, ttf)
roll2 = RollLockydraw(namelists, ttf)
roll3 = RollLockydraw(namelists, ttf)
roll.setsound("./music/sound1.wav")
def func():
	global count
	global x
	global y
	global max_x
	global screen
	if count%3==0:
		y -= 1
	# 	x +=1
	# 	x %= max_x
	# 	y = max_x - x
	count +=1
	# if y<=3:
	# 	if roll.getrolling()>3:
	# 		y = 3
	# 	elif roll.getrolling()<3:
	# 		y = 0
	# 		print ">:", roll.getptr()
	# 		roll.remove(roll.getptrname())
	# 		y = 40
	# 		print namelists
	if y<=0:
		y=0
	y =2
	roll.rolling(y)
	# roll2.rolling(y)
	# roll3.rolling(y)
	roll.blit(screen, (40,100))
	# roll2.blit(screen, (140,100))
	# roll3.blit(screen, (240,100))

def main():
	clock_old = 0
	global bg
	global bg2
	while 1:
		time.sleep(0.001)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print u'exit'
				exit()
			if event.type == VIDEORESIZE:
				SCREEN_SIZE = event.size
				screen == pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
				pygame.display.set_caption("Window resized to " + str(event.size))

				bg2 = pygame.transform.smoothscale(bg, SCREEN_SIZE)

		# func()
		if time.clock() - clock_old>=0.025:
			clock_old = time.clock()

		screen.blit(bg2, (0, 0))

			# func()

		pygame.display.update()

		# print time.clock()
		

	pass

if __name__ == '__main__':
	main()