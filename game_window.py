import pygame

x = int(input("How wide? "))
y = int(input("How tall? "))

screen = pygame.display.set_mode([x,y])
running = True

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False