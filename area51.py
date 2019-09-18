
import pygame, time

# AQUI SÃO DEFINIDAS AS CORES QUE SERÃO USADAS POSTERIORMENTE
class cor():

    vermelha = (227, 57, 9)
    cinza = (150, 150, 150)
    roxo = (128, 0, 128)
    amarelo = (255, 215, 0)
    amarelo_dark = (239, 164, 18)
    amarelo_higth = (208, 224, 69)
    black = (10, 19, 1)

# AQUI SÃO DEFINIDAS AS VARIAVEIS QUE RECEBEM OS OBJETOS
class objeto():

    ret = pygame.Rect(20, 10, 50, 50)
    lat_left = pygame.Rect(0, 0, 3, 650)
    lat_right = pygame.Rect(597, 0, 3, 650)
    ret2 = pygame.Rect(0, 108, 500, 15)
    ret3 = pygame.Rect(90, 213, 510, 15)
    ret4 = pygame.Rect(0, 308, 530, 15)
    ret5 = pygame.Rect(70, 398, 530, 15)
    ret6 = pygame.Rect(0, 479, 540, 15)
    ret7 = pygame.Rect(60, 552, 540, 15)
    chegada = pygame.Rect(565, 569, 30, 49)
    chegada2 = pygame.Rect(475, 569, 90, 49)
    rodape = pygame.Rect(0, 620, 600, 30)

# NESTA CLASSE AS VARIAVEIS RECEBEM OS ARQUIVOS QUE SERÃO USADOS
class arq():
    fundo = pygame.image.load('/home/mateus/Documentos/scripts/python/area51/ovni_fundo.png')
    freira = pygame.image.load('/home/mateus/Documentos/scripts/python/area51/freira_susto.jpg')
    freira_fim = pygame.image.load('/home/mateus/Documentos/scripts/python/area51/freira_fim.jpg')
    nave = pygame.image.load('/home/mateus/Documentos/scripts/python/area51/ovni.png')

# FUNÇÃO QUE RENDERIZA A IMAGEM DE FUNDO DO JOGO
def img_fundo():

        tela.blit(sup, [0, 0])
        sup.fill(cor.black)
        sup.blit(arq.fundo, [-100, -50])

# FUNÇÃO QUE CHAMA A FUNÇÃO DA FREIRA QUANDO EXISTIR COLISÃO
def freira():

    for x in range(120):
        tela.blit(sup, [0, 0])
        sup.fill(cor.black)
        sup.blit(arq.freira, [-120, 40])
        pygame.display.update()
        relogio.tick(30)

# FUNÇÃO QUE CHAMA UM EFEITO FINAL QUANDO O JOGADOR CHEGA NO FIM DO JOGO
def freira_fim():

    for x in range(100):
        tela.blit(sup, [0, 0])
        sup.fill(cor.black)
        sup.blit(arq.freira_fim, [-100, -50])
        pygame.display.update()
        relogio.tick(10)


def som_fundo():

    pygame.mixer.music.load('/home/mateus/Documentos/scripts/python/area51/toque_fundo.mp3')
    pygame.mixer.music.play(3)


def som_piano():

    pygame.mixer.music.load('/home/mateus/Documentos/scripts/python/area51/piano.mp3')
    pygame.mixer.music.play()


def grito():

    pygame.mixer.music.load('/home/mateus/Documentos/scripts/python/area51/toque_grito.mp3')
    pygame.mixer.music.play()

# NAS PROXIMAS LINHAS A TELA E A SURFACE SÃO CRIADAS, TAMBÉM É CRIADA A STRINGS QUE SERA EXIBIDA
pygame.init()

tela = pygame.display.set_mode([600, 650])
pygame.display.set_caption('ÁREA 51')

sup = pygame.Surface((600, 650))
sup.fill(cor.black)

relogio = pygame.time.Clock()
som_fundo()

pygame.font.init()

font_padrao = pygame.font.get_default_font()
fonte_A = pygame.font.SysFont(font_padrao, 45)
fonte_B = pygame.font.SysFont(font_padrao, 26)

sair = True
contador = 0

# INICIO DO LOOP DO JOGO
while sair == True:

    # EVENTO QUE CAPTURA QUANDO O BOTÃO FECHAR É CLICADO
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False

    relogio.tick(30)
    img_fundo()

    # AQUI É CRIADO O CENARIO, CHAMANDO OS OBJETOS
    pygame.draw.rect(tela, cor.vermelha, objeto.ret)
    pygame.draw.rect(tela, cor.amarelo, objeto.ret2)
    pygame.draw.rect(tela, cor.amarelo, objeto.ret3)
    pygame.draw.rect(tela, cor.amarelo, objeto.ret4)
    pygame.draw.rect(tela, cor.amarelo, objeto.ret5)
    pygame.draw.rect(tela, cor.amarelo, objeto.ret6)
    pygame.draw.rect(tela, cor.amarelo, objeto.ret7)
    pygame.draw.rect(tela, cor.amarelo, objeto.lat_left)
    pygame.draw.rect(tela, cor.amarelo, objeto.lat_right)
    pygame.draw.rect(tela, cor.amarelo, objeto.rodape)
    pygame.draw.rect(tela, cor.amarelo_dark, objeto.chegada)
    pygame.draw.rect(tela, cor.amarelo_higth, objeto.chegada2)
    texto = fonte_B.render('CHEGADA', 1, (27,36,94))
    tela.blit(texto, (477, 585))

    # COMANDO PARA O OBJETO PRINCIPAL SEGUIR O MOUSE
    (objeto.ret.left, objeto.ret.top) = pygame.mouse.get_pos()
    objeto.ret.left -= objeto.ret.width / 2
    objeto.ret.top -= objeto.ret.height / 2

    # ESTRUTURA QUE CAPTURA A EXISTÊNCIA DE COLISÃO
    if objeto.ret.colliderect(objeto.lat_right) or objeto.ret.colliderect(objeto.lat_left) or  objeto.ret.colliderect(objeto.ret2) or objeto.ret.colliderect(objeto.ret3) or objeto.ret.colliderect(objeto.ret4) or objeto.ret.colliderect(objeto.ret5) or objeto.ret.colliderect(objeto.ret6) or objeto.ret.colliderect(objeto.ret7) or objeto.ret.colliderect(objeto.rodape):
        if contador == 0:
            (objeto.ret.left, objeto.ret.top) = (10, 30)
            pygame.mouse.set_pos(35, 55)
            contador += 1
        else:
            (objeto.ret.left, objeto.ret.top) = (10, 30)
            pygame.mouse.set_pos(35, 55)
            grito()
            freira()
            som_fundo()

    # ESTRUTURA QUE CAPTURA SE O JOGADOR CONSEGUIU ATINGIR O OBJETIVO E CHAMA A FUNÇÃO DE FIM DE JOGO
    if objeto.ret.colliderect(objeto.chegada2):
        som_piano()
        freira_fim()
        grito()
        freira()
        sair = False

    pygame.display.update()

pygame.quit()
