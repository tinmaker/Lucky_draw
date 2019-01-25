import pygame
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((600, 400), RESIZABLE, 32)
clock = pygame.time.Clock()
def main():

	while 1:      
		event_list = pygame.event.get()
		for event in event_list:
			if event.type == QUIT:
				pygame.quit()
				exit()
			if event.type == KEYDOWN:
				print event.key, K_KP0
			if event.type == MOUSEBUTTONDOWN:
				print pygame.mouse.get_pressed()
		print event_list
		screen.fill((255,255,255))
		pygame.display.update()
		pass
		clock.tick(1)
if __name__ == '__main__':
	main() 