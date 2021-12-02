import pygame
import sys

pygame.init()


tamanho = comprimento, altura = 600, 600
janela = pygame.display.set_mode(tamanho)


xis = pygame.image.load("xis.png")
bola = pygame.image.load("bola.png")

xis = pygame.transform.scale(xis, (100,100))
bola = pygame.transform.scale(bola,(100,100))


Preto = 0, 0, 0
Branco = 255, 255, 255
Vermelho = 255, 0, 0
Verde = 0, 255, 0
Azul = 0, 0, 255

cores = [Preto, Branco, Vermelho, Verde, Azul]

vez = 'X'
rodada = 0
vencedor1 = ''

jogo = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'], ]


quadrante_linha = [50 , 250, 450]
quadrante_coluna = [50, 250, 450]

#Preenche a janela (0: preto - 1: branco - 2: vermelho - 3: verde - 4:azul )
janela.fill(cores[4]) 


def desenha_quadro():
    pygame.draw.line(janela, Preto, (200,0),(200,600),15)
    pygame.draw.line(janela, Preto, (400,0),(400,600),15)
    pygame.draw.line(janela, Preto, (0,200),(600,200),15)
    pygame.draw.line(janela, Preto, (0,400),(600,400),15)



def faz_bola(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    
    if (jogo[index_coluna][index_linha] == '_'):
        janela.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        jogo[index_coluna][index_linha] = 'O'
        return True
    else:
        print('ocupada')
        return False


def faz_xis(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)

    if (jogo[index_coluna][index_linha] == '_'):
        janela.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        jogo[index_coluna][index_linha] = 'X'
        return True

    else:
        print('ocupada')
        return False


def ganhou1():
    vencedor = ''
    

    if (jogo[0][0]== "X") and (jogo[0][1]== "X") and (jogo[0][2]== "X"):
        print ("X GANHOU!!!")
        pygame.draw.line(janela, Vermelho,(0,100), [600,100], 15)
      
        vencedor = 'X'
    if (jogo[1][0] == "X") and (jogo[1][1]== "X") and (jogo[1][2] == "X"):
        print ("X GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (0, 300), (600, 300), 15)
    
        vencedor = 'X'
    if (jogo[2][0] == "X") and (jogo[2][1] == "X") and(jogo[2][2] == "X"):
        print ("X GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (0, 500), (600, 500), 15)
     
        vencedor = 'X'

   
    if (jogo[0][0] == "X") and (jogo[1][0] == "X") and(jogo[2][0] == "X"):
        print (" X GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (100, 0), (100, 600), 15)
        vencedor = 'X'
    if (jogo[0][1] == "X") and (jogo[1][1] == "X") and(jogo[2][1] == "X"):
        print ("X GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (300, 0), (300, 600), 15)
        vencedor = 'X'
    if (jogo[0][2] == "X") and (jogo[1][2] == "X") and(jogo[2][2] == "X"):
        print ("X GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (500, 0), (500, 600), 15)
        vencedor = 'X'


    if (jogo[0][0] == "X") and (jogo[1][1] == "X") and (jogo[2][2] == "X"):
        print ("X GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (0, 0), (600, 600), 15)
        vencedor = 'X'
    if (jogo[0][2] == "X") and (jogo[1][1] == "X") and (jogo[2][0] == "X"):
        print (" X GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (0, 600), (600, 0), 15)
        vencedor = 'X'    
    return vencedor

def ganhou2():
    vencedor = ''

    if (jogo[0][0]== "O") and (jogo[0][1]== "O") and (jogo[0][2]== "O"):
        print ("O GANHOU!!!")
        pygame.draw.line(janela, Vermelho,(0,100), [600,100], 15)
        vencedor = 'O'
    if (jogo[1][0] == "O") and (jogo[1][1]== "O") and (jogo[1][2] == "O"):
        print (" 1 GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (0, 300), (600, 300), 15)
        vencedor = 'O'
    if (jogo[2][0] == "O") and (jogo[2][1] == "O") and(jogo[2][2] == "O"):
        print ("1 GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (0, 500), (600, 500), 15)
        vencedor = 'O'


    if (jogo[0][0] == "O") and (jogo[1][0] == "O") and(jogo[2][0] == "O"):
        print ("O GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (100, 0), (100, 600), 15)
        vencedor = 'O'
    if (jogo[0][1] == "O") and (jogo[1][1] == "O") and(jogo[2][1] == "O"):
        print (" O GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (300, 0), (300, 600), 15)
        vencedor = 'O'
    if (jogo[0][2] == "O") and (jogo[1][2] == "O") and(jogo[2][2] == "O"):
        print (" O GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (500, 0), (500, 600), 15)
        vencedor = 'O'


    if (jogo[0][0] == "O") and (jogo[1][1] == "O") and (jogo[2][2] == "O"):
        print (" O GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (0, 0), (600, 600), 15)
        vencedor = 'O'
    if (jogo[0][2] == "O") and (jogo[1][1] == "O") and (jogo[2][0] == "O"):
        print (" O GANHOU!!!")
        pygame.draw.line(janela, Vermelho, (0, 600), (600, 0), 15)
        vencedor = 'O'    
    return vencedor




while True:
    desenha_quadro()

    
    #Verifica eventos na janela do jogo
    for event in pygame.event.get():
     
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
                        
    #Vez de cada jogador
            if (vez=='X'):
                print("Vez de X")
                fez_jogada = faz_xis(click_pos)
                vencedor1= ganhou1()
                if (fez_jogada == True):
                    vez='O'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'X'
                    
                
            elif (vez=='O'):
                print("Vez de O")
                fez_jogada = faz_bola(click_pos)
                vencedor1= ganhou2()
                if (fez_jogada == True):
                    vez = 'X'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'O'
                    
    pygame.display.flip() #Atualiza a janela

    #Verifica se há vencedores ou não
    if (rodada>=9) and (vencedor1==''):
        print("veia!")
        print(jogo)
        break
    
    elif (vencedor1!=''):
        print(jogo)
        break
