import pygame
from config import GAME_NAME,WHITE,FPS,QUIT,GAME,BLACK,FONTEP,FONTEG,FONTEM

def init_screen(screen):
    clock = pygame.time.Clock()

    text1 = FONTEG.render(GAME_NAME, True, WHITE)
    text2 = FONTEM.render("Pressione qualquer tecla para iniciar", True, WHITE)

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

def game_controls(screen):

	gcont = True

	while gcont:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


		screen.fill(white)
		message_to_screen("Controls", 
			green,
			-100,
			"large")

		message_to_screen("Fire: Spacebar",
			black,
			-30)
		message_to_screen("Move Turret: Up and Down arrows",
			black,
			10)
		message_to_screen("Move Tank: Left and Right arrows",
			black,
			50)

		message_to_screen("Pause: P",
			black,
			90)

		button("play", 150, 500, 100, 50, green, light_green, action="play")
		button("Main", 350, 500, 100, 50, yellow, light_yellow, action="main")
		button("quit", 550, 500, 100, 50, red, light_red, action="quit")

		pygame.display.update()
		clock.tick(15)