import pygame

pygame.init()

#cores
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (34,177,76)

FPS = 15

WIDTH = 800
HEIGHT = 600
APPLESIZE = 20
SIZE = 20

fontp = pygame.font.SysFont('dejavusansmono',20)
fontm = pygame.font.SysFont('dejavusansmono',30)
fontg = pygame.font.SysFont('dejavusansmono',60)

#gameDisplay.blit(head, (S_list[-1][0],S_list[-1][1]))
 #   for XeY in S_list[:-1]:
  #      pygame.draw.rect(gameDisplay,green,[XeY[0],XeY[1],SIZE,SIZE])