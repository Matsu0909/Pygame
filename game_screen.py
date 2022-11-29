import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, TURN, WINNER
from assets import load_assets, BACKGROUND
from sprites import Tank1, Tank2, Explosion1, Explosion2

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_players = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_bullets'] = all_bullets
    groups['all_players'] = all_players

    # Criando o jogador
    player1 = Tank1(groups, assets)
    all_sprites.add(player1)
    all_players.add(player1)

    player2 = Tank2(groups,assets)
    all_sprites.add(player2)
    all_players.add(player2)
    
    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                #Turno
                if TURN == 1:
                    player = player1

                if TURN == 2:
                    player = player2
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_SPACE:
                        player.shoot()

                        #Troca de turno
                        if TURN == 2:
                            TURN = 1
                        elif TURN == 1:
                            TURN = 2

                    if event.key == pygame.K_UP:
                        if player.angle < 86 and player.angle >= 0:
                            player.angle += 5
                    if event.key == pygame.K_DOWN:
                        if player.angle < 86 and player.angle >= 0:
                            player.angle -= 5
                    if event.key == pygame.K_p:
                        if player.power < 10:
                            player.power += 1
                    if event.key == pygame.K_o:
                        if player.power > 0:
                            player.power -= 1

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        if state == PLAYING:
            # Verifica se houve colisão entre nave e tiro
            for player in all_players:

                hits = pygame.sprite.spritecollide(player, all_bullets, True, pygame.sprite.collide_mask)
                if len(hits) > 0:
                # Toca o som da colisão
                    player.kill()
                    if player == player1:
                        Explosion = Explosion1
                    else:
                        Explosion = Explosion2
                    explosao = Explosion(player.rect.center, assets)
                    all_sprites.add(explosao)
                    state = EXPLODING
                    keys_down = {}
                    explosion_tick = pygame.time.get_ticks()
                    explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400

                    #Tela de vitória
                    if player == player1:
                        WINNER = 'Player 2'
                    else:
                        WINNER = 'Player 1'

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor preta
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)

        pygame.display.update()  # Mostra o novo frame para o jogador
