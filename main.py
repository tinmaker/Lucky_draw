import pygame
from pygame.locals import *
from rollLockydraw import *
import time

pygame.init()

namelists = ["111", "222", "333", "444", "555", "666", "777"]
# namelists = ["111", "222", "333"]
pygame.init()
ttf = "myfont.ttf"
def main():
	screen = pygame.display.set_mode((600, 600),RESIZABLE,32)
	roll = RollLockydraw(namelists, ttf)
	while 1:
		time.sleep(0.05)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print u'exit'
				exit()
		roll.subptr(1)
		screen.fill((255,255,255))
		roll.blit(screen, (100,100))
		pygame.display.update()

	pass

if __name__ == '__main__':
	main()