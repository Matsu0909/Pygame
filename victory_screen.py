import pygame
from config import GAME_NAME,WHITE,FPS,QUIT,GAME,BLACK,FONTEM,FONTEG,FONTEP
from game_screen import WINNER

def victory_screen(screen):
    clock = pygame.time.Clock()

    text1 = FONTEG.render(WINNER, True, WHITE)
    text2 = FONTEM.render('Parabéns você ganhou!', True, WHITE)

    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = QUIT
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(text1, (70, 250))
        screen.blit(text2, (70, 500))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state