import pygame

x = int(input("How wide? "))
y = int(input("How tall? "))

screen = pygame.display.set_mode([x,y])

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	screen.fill((255, 255, 255))
	pygame.display.flip()