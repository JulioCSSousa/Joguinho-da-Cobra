import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

point = pygame.mixer.Sound('smw_fireball.wav')
#point.set_volume(0 ate 1)
musicaback = pygame.mixer.music.load('BoxCat Games - Inspiration.mp3')
pygame.mixer.music.play(-1)

altura = 800
largura = 600
x_snake = int(altura/2)
y_snake = int(largura/2)
x_apple = randint(20,780)
y_apple = randint(20,580)
vel = 10
x_controle = vel
y_controle = 0

relogio = pygame.time.Clock()

pontos = 0


fonte = pygame.font.SysFont('arial',40,bold=True,italic=True )

tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Jogo de quadrados')
comprimento = 20
def cobra_up(lista_snake):
    for XeY in lista_snake:
        pygame.draw.rect(tela, (0,255,0), (XeY[0],XeY[1],20,20))
def reiniciar():
    global comprimento, x_snake,y_snake,lista_snake,lista_head,x_apple,y_apple,morreu
    pontos = 0
    comprimento = 20
    x_snake = int(altura/2)
    y_snake = int(largura/2)
    lista_snake = []
    lista_head = []
    x_apple = randint(20,780)
    y_apple = randint(20,580)
    morreu = False
morreu = False

lista_snake = []

#loop que mantem a tela
while True:
    relogio.tick((30))
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT: #Sair do programa
            pygame.quit()
            exit()

        #controles
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == vel:
                    pass
                else:
                    x_controle = -vel
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -vel:
                    pass
                else:
                    x_controle = vel
                    y_controle = 0
            if event.key == K_w:
                if y_controle == vel:
                    pass
                else:
                    x_controle = 0
                    y_controle = -vel
            if event.key == K_s:
                if y_controle == -vel:
                    pass
                else:
                    x_controle = 0
                    y_controle = vel
    x_snake = x_snake + x_controle
    y_snake = y_snake + y_controle

    snake = pygame.draw.rect(tela,(0, 255, 0), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(tela, (255,0,0),(x_apple, y_apple, 20, 20))

    #colisao com a maçã
    if snake.colliderect(apple):
        pontos += 1
        x_apple= randint(20,780)
        y_apple = randint(20,580)
        point.play()
        comprimento += 1
        vel += 0.3
    cobra_up(lista_snake)
    #controle do len da cobra
    if len(lista_snake) > 20:
        del lista_snake[0]

    #aumento da cobra
    lista_head = []
    lista_head.append(x_snake)
    lista_head.append(y_snake)
    lista_snake.append(lista_head)

    if lista_snake.count(lista_head) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True,True)
        mensagem = 'Game Over! Apert "r" para jogar novamente'
        texto2 = fonte2.render(mensagem, True, (255,0,0))
        morreu = True
        ret_text = texto2.get_rect()
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            ret_text.center = (altura//2, largura//2)
            tela.blit(texto2, (ret_text))
            pygame.display.update()
    if x_snake > altura:
        x_snake = 0
    if x_snake < 0:
        x_snake = altura
    if y_snake < 0:
        y_snake = largura
    if y_snake > largura:
        y_snake = 0
    tela.blit(texto, (550,50))

    pygame.display.update() #loop que detecta cada update de tela

