import pygame
from config import GAME_NAME,WHITE,FPS,QUIT,GAME,BLACK,FONTEP,FONTEG,FONTEM

def init_screen(screen):
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 48)
    text1 = font.render(GAME_NAME, True, WHITE)
    text2 = font.render("Pressione qualquer tecla para iniciar", True, WHITE)

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
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(text1, (70, 250))
        screen.blit(text2, (70, 500))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state