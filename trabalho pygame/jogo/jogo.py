#Trabalho desenvolvido por João Pedro Ribeiro e Guilherme Silvestre Giazzi

import sys
import pygame
import random
pygame.mixer.pre_init(22050, -16, 2, 64)
pygame.mixer.init()
pygame.init()
screen_width = 1200
screen_height = 600
SCREEN = pygame.display.set_mode((screen_width,screen_height))
BLACK = (0,0,0)
WHITE = (250,250,250)

aux = 20 #variável auxiliar para a contagem do tempo para recarregar munição
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT + 1, 1)  #MOVIMENTADOR DE BALAS
pygame.time.set_timer(pygame.USEREVENT + 2, 50)  #MOVIMENTADOR DE ZUMBIS
balaImage = pygame.image.load("imagens/sprite_bala.png")
balaImage2 = pygame.image.load("imagens/sprite_bala2.png")

Balas = []
#pygame.time.set_timer(pygame.USEREVENT+3, 1000)
#tela_final = pygame.image.load("imagens/tela_final.png")

score = 0
font = pygame.font.SysFont("Verdana", 30)

#--------------RANKING--------------#
col_jogador = font.render("Jogador", 1, (WHITE))
col_tempo = font.render("Tempo",1 , (WHITE))
col_nivel = font.render("Nivel", 1, (WHITE))
col_score = font.render("Pontuação",1, (WHITE))
#----------^RANKING^-----------------#

personagemImage = pygame.image.load("imagens/sprite_personagem.png")
Personagem = [pygame.transform.flip(personagemImage, 1, 0 ), personagemImage.get_rect(), 0]
Personagem[1].left = 500
Personagem[1].top = 400

fundo_ranking = pygame.image.load("imagens/fundo_ranking.jpeg")

chao = pygame.image.load("imagens/chao4.png")
bg = pygame.image.load("imagens/tela_fundo.jpg")
bg2 = pygame.image.load("imagens/fundo2.jpg")
bg3 = pygame.image.load("imagens/fundo3.jpg")
lives = pygame.image.load("imagens/sprite_vida.png")
image_vr_ranking = pygame.image.load("imagens/btn_ranking.png")
image_jogar_novamente = pygame.image.load("imagens/btn_novamente.png")
btn_voltar = pygame.image.load("imagens/btn_voltar.png")
instImage = pygame.image.load('imagens/tela_instrucoes.png')
vida = 3
time = 0
timef = 0
ammo = 10
nivel = 1
zumbiImage = pygame.image.load("imagens/zumbi_nvl1.png")
zumbiImage2 = pygame.image.load("imagens/zumbi_nvl1_2.png")

zumbi_n2 = pygame.image.load("imagens/zumbi_nvl2.png")
zumbi_n2_2 = pygame.image.load("imagens/zumbi_nvl2_2.png")

zumbi_n3 = pygame.image.load("imagens/zumbi_nvl3.png")
zumbi_n3_2 = pygame.image.load("imagens/zumbi_nvl3_2.png")

zumbi_n4 = pygame.image.load("imagens/zumbi_nvl4.png")
zumbi_n4_2 = pygame.image.load("imagens/zumbi_nvl4_2.png")

zumbi_n5 = pygame.image.load("imagens/zumbi_nvl5.png")
zumbi_n5_2 = pygame.image.load("imagens/zumbi_nvl5_2.png")

vida_zumbi = 1
lstZumbis = []
spawnPoint1 = ((-85, 405), (1230, 405))
spawnPoint2 = ((-95, 375), (1230, 375))
spawnPoint3 = ((-85, 395), (1230, 395))
spawnPoint4 = ((-85, 385), (1230, 385))
spawnPoint5 = ((-85, 345), (1230, 345))

players = []
player_num = 1
play = pygame.image.load('imagens/btn_play.png')
instr = pygame.image.load('imagens/btn_instrucoes.png')

#música de início
pygame.mixer.music.load('before.mp3')
pygame.mixer.music.play()


def setup():
    global vida
    global time
    global score
    global lstZumbis
    global keepPressing
    global Balas
    global ammo
    global nivel
    vida = 3
    time = 0
    score = 0
    lstZumbis = []
    keepPressing = []
    Balas = []
    ammo = 10
    nivel = 1
    Personagem[1].left = 500
    Personagem[1].top = 400
def move_personagem(x):
    Personagem[1].left += x
    Personagem[1].left = max(-10, Personagem[1].left)
    Personagem[1].left = min(1120, Personagem[1].left)


def ESCOLHER_LADO():
    return random.randint(0,1)

def spawn_zumbi():
    lado = ESCOLHER_LADO()
    if nivel == 1:
        if lado == 0:
            Zumbi = [zumbiImage2.copy(), zumbiImage.get_rect()]
        else:
            Zumbi = [zumbiImage.copy(), zumbiImage.get_rect()]
        Zumbi[1].left, Zumbi[1].top = spawnPoint1[lado][0], spawnPoint1[lado][1]
        lstZumbis.append(Zumbi)
        
    elif nivel == 2:
        if lado == 0:
            Zumbi = [zumbi_n2_2.copy(), zumbi_n2.get_rect()]
        else:
            Zumbi = [zumbi_n2.copy(), zumbi_n2.get_rect()]
        Zumbi[1].left, Zumbi[1].top = spawnPoint2[lado][0], spawnPoint2[lado][1]
        lstZumbis.append(Zumbi)

    elif nivel == 3:
        if lado == 0:
            Zumbi = [zumbi_n3_2.copy(), zumbi_n3.get_rect()]
        else:
            Zumbi = [zumbi_n3.copy(), zumbi_n3.get_rect()]
        Zumbi[1].left, Zumbi[1].top = spawnPoint3[lado][0], spawnPoint3[lado][1]
        lstZumbis.append(Zumbi)

    elif nivel == 4:
        if lado == 0:
            Zumbi = [zumbi_n4_2.copy(), zumbi_n4.get_rect()]
        else:
            Zumbi = [zumbi_n4.copy(), zumbi_n4.get_rect()]
        Zumbi[1].left, Zumbi[1].top = spawnPoint4[lado][0], spawnPoint4[lado][1]
        lstZumbis.append(Zumbi)

    elif nivel == 5:
        if lado == 0:
            Zumbi = [zumbi_n5_2.copy(), zumbi_n5.get_rect()]
        else:
            Zumbi = [zumbi_n5.copy(), zumbi_n5.get_rect()]
        Zumbi[1].left, Zumbi[1].top = spawnPoint5[lado][0], spawnPoint5[lado][1]
        lstZumbis.append(Zumbi)

def spawn_bala(direcao):
    if direcao == 0:
        #pygame.transform.flip(balaImage, 1, 0)
        bala = [balaImage2.copy(), balaImage.get_rect(), direcao]
    else:
        bala = [balaImage.copy(), balaImage.get_rect(), direcao]
    bala[1].left = Personagem[1].left
    bala[1].top = 480
    Balas.append(bala)
#função que dá 8 munições ao joador, após 20 segundos
def add_ammo():
    global aux
    if int(timef) >= int(aux):
        global ammo
        global nivel
        ammo += 10
        aux += 20
        nivel += 1


def desenha_chao():
    SCREEN.blit(chao,(0,500))


def chama_vidas():
    for i in range(vida):
        SCREEN.blit(lives, (820 + (80*i), 0))
player = [0, 0, 0, 0]

cont = 0
ver_ranking = False
game_running = False
keepPressing = []
instrucoes = False
menu = True
final = False
while True:
    
    while menu:
        SCREEN.fill(WHITE)
        SCREEN.blit(bg2, (0, 0))
        SCREEN.blit(play, (450, 200))
        SCREEN.blit(instr, (450, 280))
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (mouse[0] > 450) and (mouse[0] < 650) and (mouse[1] > 200) and (
                mouse[1] < 250):
                if event.type == pygame.MOUSEBUTTONUP:
                    menu = False
                    game_running = True
                    #música durante o jogo
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('during.mp3')
                    pygame.mixer.music.play()

            if (mouse[0] > 450) and (mouse[0] < 650) and (mouse[1] > 280) and (
                mouse[1] < 330):
                if event.type == pygame.MOUSEBUTTONUP:
                    instrucoes = True
                    menu = False
    while instrucoes:
        mouse = pygame.mouse.get_pos()
        SCREEN.fill(WHITE)
        SCREEN.blit(instImage, (0, 0))
        SCREEN.blit(btn_voltar, (500, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (mouse[0] > 500) and (mouse[0] < 700) and (mouse[1] > 500) and (mouse[1] <550):
                if event.type == pygame.MOUSEBUTTONUP:
                    instrucoes = False
                    menu = True

    while game_running:

        jogador = font.render("Jogador "+str(player[0]+1), True, (255,255,255))


        timer = font.render('Tempo: '+str(timef), True, (255, 255, 255))
        SCREEN.fill(WHITE)
        SCREEN.blit(bg, (0, 0))
        text = font.render("Pontuação: " + str(score), True, (255,255,255))
        municao = font.render("Munição: " + str(ammo), True, (255,255,255))
        nivel_jog = font.render("Nível: " + str(nivel), True, (255,255,255))
        SCREEN.blit(municao, [20, 100])
        SCREEN.blit(text, [20, 50])
        SCREEN.blit(jogador, [20, 200])
        SCREEN.blit(nivel_jog, [20, 5])

        chama_vidas()
        balar = balaImage.get_rect()
        desenha_chao()
        add_ammo()
        SCREEN.blit(timer,[20, 150])
        for zumbi in lstZumbis:
            SCREEN.blit(zumbi[0], zumbi[1])
            if zumbi[1].colliderect(Personagem[1]):
                vida -= 1
                lstZumbis.remove(zumbi)
                if vida == 0:

                    player = [player_num, timef, nivel, score]
                    if len(players) == 5:
                        check = [players[i][1] for i in range(len(players))]
                        for i in range(len(check)):
                            if check[i] < player[1]:
                                players[i] = player
                                break
                    elif len(players) < 5:
                        players.append(player)
                    player_num += 1



                    final = True
                    game_running = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('after.mp3')
                    pygame.mixer.music.play()
        for bala in Balas:
            SCREEN.blit(bala[0], bala[1])
            if bala[1].colliderect(zumbi[1]):
                cont += 1
                Balas.remove(bala)
                if nivel == 1:
                    lstZumbis.remove(zumbi)
                    score += 1
                    cont = 0
                elif nivel == 2:
                    if cont == 2:
                        lstZumbis.remove(zumbi)
                        score += 1
                        cont = 0
                elif nivel == 3:
                    if cont == 3:
                        lstZumbis.remove(zumbi)
                        score += 1
                        cont = 0
                elif nivel == 4:
                    if cont == 4:
                        lstZumbis.remove(zumbi)
                        score += 1
                        cont = 0
                elif nivel == 5:
                    if cont == 5:
                        lstZumbis.remove(zumbi)
                        score += 1
                        cont = 0
                    
        for key in keepPressing:
            if key in keepPressing:
                if key == pygame.K_LEFT:
                    if Personagem[2] == 1:
                        Personagem[0] = pygame.transform.flip(Personagem[0], 1, 0 )
                        Personagem[2] = 0
                    move_personagem(-4)
                elif key == pygame.K_RIGHT:
                    if Personagem[2] == 0:
                        Personagem[0] = pygame.transform.flip(Personagem[0], 1, 0 )
                        Personagem[2] = 1
                    move_personagem(4)
        if len(lstZumbis) == 0:
            spawn_zumbi()
       
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(),
            elif event.type == pygame.USEREVENT + 1:
                time += 1 / 100
                timef = format(time,'.0f')
                for bala in Balas:
                    if bala[2] == 0:
                        bala[1].left -= 5
                    else:
                        bala[1].left += 5
            elif event.type == pygame.USEREVENT + 2:
                for zumbi in lstZumbis:
                    valor = 0
                    if zumbi[1].left > Personagem[1].left:
                        valor = -5
                        valor = -5
                    else:
                        valor = 5
                    zumbi[1].left += valor
            elif event.type == pygame.KEYDOWN:
                keepPressing.append(event.key)
                if event.key == pygame.K_z:
                    if ammo > 0:
                        spawn_bala(Personagem[2])
                        ammo -= 1
                        keepPressing.remove(event.key)
                    else:
                        ammo = 0

            elif event.type == pygame.KEYUP:
                if event.key in keepPressing:
                    keepPressing.remove(event.key)
        SCREEN.blit(Personagem[0], Personagem[1])
        pygame.display.update()
        nivel_final = font.render("Você chegou ao nível: " + str(nivel), 1, (WHITE))
        pontuacao = font.render("Sua pontuação foi: " + str(score), 1, (WHITE))
        tempo_final = font.render("Seu tempo final foi: "+str(timef)+" segundos", 1, (WHITE))
    while final:
        SCREEN.fill(WHITE)
        SCREEN.blit(bg3, (0, 0))
        #SCREEN.blit(tela_final,(0, 0))
        SCREEN.blit(pontuacao, (300, 300))
        SCREEN.blit(nivel_final, (300, 100))
        SCREEN.blit(tempo_final, (300 , 200))
        SCREEN.blit(image_jogar_novamente, (300, 400))
        SCREEN.blit(image_vr_ranking, (300, 450))
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if (mouse[0] > 300) and (mouse[0] < 500) and (mouse[1] > 450) and (mouse[1] < 500):
                if event.type == pygame.MOUSEBUTTONUP:
                    final = False
                    ver_ranking = True
            if (mouse[0] > 300) and (mouse[0] < 500) and (mouse[1] > 400) and (mouse[1] < 450):
                if event.type == pygame.MOUSEBUTTONUP:


                    final = False
                    setup()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('during.mp3')
                    pygame.mixer.music.play()
                    game_running = True

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    while ver_ranking:
        #---------RENDER DAS LINHAS--------#
        linha1_1 = font.render(str(players[0][0]), 1, (WHITE))
        linha1_2 = font.render(str(players[0][1]), 1, (WHITE))
        linha1_3 = font.render(str(players[0][2]), 1, (WHITE))
        linha1_4 = font.render(str(players[0][3]), 1, (WHITE))
        if len(players) > 1:
            linha2_1 = font.render(str(players[1][0]), 1, (WHITE))
            linha2_2 = font.render(str(players[1][1]), 1, (WHITE))
            linha2_3 = font.render(str(players[1][2]), 1, (WHITE))
            linha2_4 = font.render(str(players[1][3]), 1, (WHITE))
            if len(players) > 2:
                linha3_1 = font.render(str(players[2][0]), 1, (WHITE))
                linha3_2 = font.render(str(players[2][1]), 1, (WHITE))
                linha3_3 = font.render(str(players[2][2]), 1, (WHITE))
                linha3_4 = font.render(str(players[2][3]), 1, (WHITE))
                if len(players) > 3:
                    linha4_1 = font.render(str(players[3][0]), 1, (WHITE))
                    linha4_2 = font.render(str(players[3][1]), 1, (WHITE))
                    linha4_3 = font.render(str(players[3][2]), 1, (WHITE))
                    linha4_4 = font.render(str(players[3][3]), 1, (WHITE))
                    if len(players) > 4:
                        linha5_1 = font.render(str(players[4][0]), 1, (WHITE))
                        linha5_2 = font.render(str(players[4][1]), 1, (WHITE))
                        linha5_3 = font.render(str(players[4][2]), 1, (WHITE))
                        linha5_4 = font.render(str(players[4][3]), 1, (WHITE))
        #--------^RENDER DAS LINHAS^--------#

        SCREEN.fill(WHITE)
        SCREEN.blit(fundo_ranking, (0, 0))
        SCREEN.blit(btn_voltar, (500, 500))
        #----LINHA 0------#
        SCREEN.blit(col_jogador, (300, 170))
        SCREEN.blit(col_tempo, (500,170))
        SCREEN.blit(col_nivel, (700,170))
        SCREEN.blit(col_score, (900,170))
        #----LINHA 1-----#
        SCREEN.blit(linha1_1, (300, 200))
        SCREEN.blit(linha1_2, (500, 200))
        SCREEN.blit(linha1_3, (700, 200))
        SCREEN.blit(linha1_4, (900, 200))
        # ----LINHA 2-----#
        if len(players) > 1:
            SCREEN.blit(linha2_1, (300, 250))
            SCREEN.blit(linha2_2, (500, 250))
            SCREEN.blit(linha2_3, (700, 250))
            SCREEN.blit(linha2_4, (900, 250))
            # ----LINHA 3-----#
            if len(players) > 2:
                SCREEN.blit(linha3_1, (300, 300))
                SCREEN.blit(linha3_2, (500, 300))
                SCREEN.blit(linha3_3, (700, 300))
                SCREEN.blit(linha3_4, (900, 300))
                # ----LINHA 4-----#
                if len(players) > 3:
                    SCREEN.blit(linha4_1, (300, 350))
                    SCREEN.blit(linha4_2, (500, 350))
                    SCREEN.blit(linha4_3, (700, 350))
                    SCREEN.blit(linha4_4, (900, 350))
                    # ----LINHA 5-----#
                    if len(players) > 4:
                        SCREEN.blit(linha5_1, (300, 400))
                        SCREEN.blit(linha5_2, (500, 400))
                        SCREEN.blit(linha5_3, (700, 400))
                        SCREEN.blit(linha5_4, (900, 400))

        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (mouse[0] > 500) and (mouse[0] < 700) and (mouse[1] > 500) and (mouse[1] < 550):
                if event.type == pygame.MOUSEBUTTONUP:
                    ver_ranking = False
                    final = True


    clock.tick(60)
