import pygame
from assets import head_img,tail_img
from config import green,fontg,fontm,fontp,WIDTH,HEIGHT,black

def snake(SIZE,S_list,direction,gameDisplay):
    if direction == 'oeste':
        head = pygame.transform.rotate(head_img,180)
        tail = pygame.transform.rotate(tail_img,180)
    
    elif direction == 'norte':
        head = pygame.transform.rotate(head_img,270)
        tail = pygame.transform.rotate(tail_img,270)

    elif direction == 'leste':
        head = pygame.transform.rotate(head_img, 0)
        tail = pygame.transform.rotate(tail_img,0)

    elif direction == 'sul':
        head = pygame.transform.rotate(head_img,90)
        tail = pygame.transform.rotate(tail_img,90)

    gameDisplay.blit(head, (S_list[-1][0],S_list[-1][1]))
    for XeY in S_list[1:-1]:
        pygame.draw.rect(gameDisplay,green,[XeY[0],XeY[1],SIZE,SIZE])
    
    if len(S_list) != 1:
        gameDisplay.blit(tail, (S_list[0][0],S_list[0][1]))

def text_objects(text,color,size):
    if size == "small":
        textSurface = fontp.render(text,True,color)
    elif size == "medium":
        textSurface = fontm.render(text,True,color)
    elif size == "large":
        textSurface = fontg.render(text,True,color)
    return textSurface, textSurface.get_rect()


def message(msg,color,gameDisplay,y_displace = 0, size='small'):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (WIDTH/2), (HEIGHT/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def score(snakeLength,gameDisplay):
    ponto = (snakeLength-1)*100
    text = 'SCORE: {0}'.format(ponto)
    textSurf, textRect = text_objects(text,black,"medium")
    textRect.center = (100),(30)
    gameDisplay.blit(textSurf,textRect)