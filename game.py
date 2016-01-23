import pygame

screen_size = height , width = 800,600

screen = pygame.display.set_mode(screen_size)

p1 = 20,20
p2 = 0,200
p3 = 300,200

pygame.draw.polygon(screen,[255,0,0],[p1,p2,p3])


while True:
	#screen.fill(black)
	#screen.blit()
	pygame.display.flip()