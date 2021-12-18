# -----------------informações do game----------------|
# tecle W, S, A ou D para se mover                    |
# sempre espere a sua vez de jogar                    |
# tecle X caso você seja o player um                  |
# tecle O caso você seja o player dois                |
# tenho que adicionar um NPC pra jogar contra o player|
# ----------------------------------------------------|

#==================BIBLIOTECAS==================|
from random import randint # <-- para o NPC    ||
from random import choice # <-- para o NPC     ||
from time import sleep # <-- contador de tempo ||
from msvcrt import getch # <-- input sem enter ||
from os import system # <-- para limpar a tela ||
#===============================================|

# --VALORES INICIAIS-------------------------------------------------------------------------------

vencedor = None 

player_ou_bot = ['PLAYER', 'BOT']
vez_do_jogador = 1
player = ['X', 'O']

casa = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
posição = 4
casa[posição] = casa[posição]

horizontal = 0
vertical = 0

fim_de_jogo = False

while fim_de_jogo == False:

    # limpar a tela--------------------------------------------------------------------------------

    system('cls')

    # REGRAS PARA GANHAR O GAME--------------------------------------------------------------------

    if  casa[0] == 'X' and casa[1] == 'X' and casa[2] == 'X' or\
        casa[3] == 'X' and casa[4] == 'X' and casa[5] == 'X' or\
        casa[6] == 'X' and casa[7] == 'X' and casa[8] == 'X' or\
        casa[0] == 'X' and casa[3] == 'X' and casa[6] == 'X' or\
        casa[1] == 'X' and casa[4] == 'X' and casa[7] == 'X' or\
        casa[2] == 'X' and casa[5] == 'X' and casa[8] == 'X' or\
        casa[0] == 'X' and casa[4] == 'X' and casa[8] == 'X' or\
        casa[2] == 'X' and casa[4] == 'X' and casa[6] == 'X':

          vencedor = 1
          fim_de_jogo = True

    elif casa[0] == 'O' and casa[1] == 'O' and casa[2] == 'O' or\
         casa[3] == 'O' and casa[4] == 'O' and casa[5] == 'O' or\
         casa[6] == 'O' and casa[7] == 'O' and casa[8] == 'O' or\
         casa[0] == 'O' and casa[3] == 'O' and casa[6] == 'O' or\
         casa[1] == 'O' and casa[4] == 'O' and casa[7] == 'O' or\
         casa[2] == 'O' and casa[5] == 'O' and casa[8] == 'O' or\
         casa[0] == 'O' and casa[4] == 'O' and casa[8] == 'O' or\
         casa[2] == 'O' and casa[4] == 'O' and casa[6] == 'O':

          vencedor = 2
          fim_de_jogo = True

    elif ' ' not in casa:
        vencedor = 0
        fim_de_jogo = True

    # indicador de posição------------------------------------------------------------------------

    if casa[posição] == " ":
        casa[posição] = '" "'

    elif casa[posição] == "X":
        casa[posição] = '"X"'

    elif casa[posição] == "O":
        casa[posição] = '"O"'

    # mapa----------------------------------------------------------------------------------------

    print(f"""
        vez do: {player_ou_bot[vez_do_jogador-1]}
                                                               
        [{casa[0]}][{casa[1]}][{casa[2]}]                 
        [{casa[3]}][{casa[4]}][{casa[5]}]   
        [{casa[6]}][{casa[7]}][{casa[8]}]    

        pressione {player[vez_do_jogador-1]}
    """)

    # tirando indicador de direção antigo---------------------------------------------------------

    if casa[posição] == '" "':
        casa[posição] = " "

    elif casa[posição] == '"X"':
        casa[posição] = "X"

    elif casa[posição] == '"O"':
        casa[posição] = "O"

    # colocando seta-------------------------------------------------------------------------------

    if fim_de_jogo != True and vez_do_jogador == 1: #input do PLAYER
        seta = getch()

    # inteligencia do bot--------------------------------------------------------------------------
    
    elif fim_de_jogo != True and vez_do_jogador == 2: #input do BOT
        
        for horizontal in range(horizontal, 6):
            
            if casa[horizontal] == 'X' and casa[horizontal+1] == 'X' and casa[horizontal+2] == ' ' or\
               casa[horizontal] == 'X' and casa[horizontal+2] == 'X' and casa[horizontal+1] == ' ' or\
               casa[horizontal+1] == 'X' and casa[horizontal+2] == 'X' and casa[horizontal] == ' ':
                
                horizontal += 3
                boleano = True
                tentativas = 0
                
                while boleano == True:

                    onde_ir = randint(horizontal, horizontal+2)            
                    tentativas += 1

                    if casa[onde_ir] == ' ' or tentativas == 9:
                        boleano = False  

                

        for vertical in range(vertical, 3):

            if  casa[vertical] == 'X' and casa[vertical+3] == 'X' or\
                casa[vertical] == 'X' and casa[vertical+6] == 'X' or\
                casa[vertical+3] == 'X' and casa[vertical+6] == 'X':

                    vertical +=1
                    boleano = True
                    tentativas = 0
                
                    while boleano == True:
                    
                        onde_ir = [vertical, vertical+3, vertical+6]
                        onde_ir = choice(onde_ir)
                        tentativas += 1

                        if casa[onde_ir] == ' ' or tentativas == 9:
                            boleano = False
            else:
                onde_ir = randint(0, 8) 

        #animação bot andando ---------------------------------------------------------------------------------

            if posição >= onde_ir + 3:
                posição = posição-3
                sleep(1/5)
            
            elif posição > onde_ir:
                posição = posição-1
                sleep(1/5)
            
            elif posição <= onde_ir - 3:
                posição = posição+3
                sleep(1/5)
            
            elif posição < onde_ir:
                posição = posição+1
                sleep(1/5)
                
    #direção--------------------------------------------------------------------------------------
    
    if  seta == b'w' and posição != 0 and posição != 1 and posição != 2 or\
        seta == b'W' and posição != 0 and posição != 1 and posição != 2 or\
        seta == b'H' and posição != 0 and posição != 1 and posição != 2:

          posição = posição-3

    elif seta == b's' and posição != 6 and posição != 7 and posição != 8 or\
         seta == b'S' and posição != 6 and posição != 7 and posição != 8 or\
         seta == b'P' and posição != 6 and posição != 7 and posição != 8:

           posição = posição+3

    elif seta == b'a' and posição != 0 or\
         seta == b'A' and posição != 0 or\
         seta == b'K' and posição != 0:

        posição = posição-1

    elif seta == b'd' and posição != 8 or\
         seta == b'D' and posição != 8 or\
         seta == b'M' and posição != 8:
         
        posição = posição+1

    # Colocando as formas no mapa----------------------------------------------------------------

    if vez_do_jogador == 1:

        if seta == b'x' and casa[posição] == ' ' or seta == b'X' and casa[posição] == ' ' or\
           seta == b'\r' and casa[posição] == ' ' or seta == b' ' and casa[posição] == ' ':
             
            casa[posição] = 'X'
            vez_do_jogador = 2
            # tempo de espera (segundos)
            sleep(1/10)

    if vez_do_jogador == 2:

        if seta == b'o' and casa[posição] == ' ' or seta == b'O' and casa[posição] == ' ' or\
           seta == b'\r' and casa[posição] == ' ' or seta == b' ' and casa[posição] == ' ':

            casa[posição] = 'O'
            vez_do_jogador = 1
            # tempo de espera (segundos)
            sleep(1/10)


# ---FIM----------------------------------------------------------------------------------------

if vencedor > 0:
    print(f'O {player_ou_bot[vencedor-1]} VENCEU!!!')

else:
    print('JOGO EMPATADO!!!')

sair = input('\ntecle enter para sair')
