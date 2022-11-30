import pygame
from assets import head_img
from config import green,fontg,fontm,fontp,WIDTH,HEIGHT
from Snake import gameDisplay

def snake(SIZE,S_list,direction):
    if direction == 'oeste':
        head = pygame.transform.rotate(head_img,180)
    
    elif direction == 'norte':
        head = pygame.transform.rotate(head_img,270)

    elif direction == 'leste':
        head = pygame.transform.rotate(head_img, 0)

    elif direction == 'sul':
        head = pygame.transform.rotate(head_img,90)

    gameDisplay.blit(head, (S_list[-1][0],S_list[-1][1]))
    for XeY in S_list[:-1]:
        pygame.draw.rect(gameDisplay,green,[XeY[0],XeY[1],SIZE,SIZE])

def text_objects(text,color,size):
    if size == "small":
        textSurface = fontp.render(text,True,color)
    elif size == "medium":
        textSurface = fontm.render(text,True,color)
    elif size == "large":
        textSurface = fontg.render(text,True,color)
    return textSurface, textSurface.get_rect()


def message(msg,color,y_displace = 0, size='small'):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (WIDTH/2), (HEIGHT/2)+y_displace
    gameDisplay.blit(textSurf, textRect)