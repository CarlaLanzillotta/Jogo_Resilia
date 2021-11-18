from time import sleep
import sys


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.5)

def quebra_linha():                                                     
    print() 
  
personagem1 = 'ANNA'
personagem2 = 'JOHN'
personagem3 = 'ANTONY'
 
descricao_personagem1 = '\nUMA HISTORIADORA CORAJOSA, LIDERA A MAIORIA DAS EXPEDIÇÕES E ADORA RESOLVER ENIGMAS.\nSEU PONTO FRACO:NÃO SABER NADAR.\n'
descricao_personagem2 = '\nEXPLORADOR NATO, SEMPRE EM BUSCA DE UMA AVENTURA NÃO MEDE ESFORÇOS PARA CONSEGUIR CONQUISTAR SEUS OBJETIVOS.\nSEU PONTO FRANCO: A TEIMOSIA.\n'
descricao_personagem3 = '\nARQUEÓLOGO,APAIXONADO POR LENDAS DE TESOUROS, É O MAIS ORGANIZADO DO GRUPO.NÃO DÁ UM PASSO SEM ANALISAR TODA SITUAÇÃO EM SUA VOLTA.\nSEU PONTO FRACO:TEM MEDO DE ALTURA.\n'



def escolha_personagem():
    global personagem
    opcao_valida = False

    while opcao_valida == False:
        personagem = int(input('\nEscolha seu Jogador: '))
       
        if personagem == 1:
            quebra_linha()
            print_slow(str(personagem1))
            quebra_linha()
            opcao_valida = True
        elif personagem == 2:
            quebra_linha()
            print_slow(str(personagem2))
            quebra_linha()
            opcao_valida =True
        elif personagem == 3:
            quebra_linha()
            print_slow(str(personagem3))
            opcao_valida = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1, 2 OU 3\n')
            quebra_linha()
            opcao_valida = False

    return personagem


def primeira_fase_jogador1():
    print('='*20 + 'FASE 1' + '='*20)
    sleep(1)
    quebra_linha()
    print('Bem-vindo a Floresta de Tugah! Preparado para a aventura?\n\n')
    print(f'{personagem1} está a beira do rio, ela deve:\n\n 1- Pular no rio '+ '    ' + ' 2- Usar uma corda\n')

    escolha_fase1 = False
    while escolha_fase1 == False:
        obstaculo_fase1 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase1 == 1: 
            print_slow(f'\nQue pena...{personagem1} escorregou nas pedras e foi levada pela correnteza!\n\nFIM DE JOGO!')
            sys.exit()
            # escolha_fase1 = True
        elif obstaculo_fase1 == 2:
            quebra_linha()
            print_slow('\nBoa escolha!Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_fase1 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase1 = False

def segunda_fase_jogador1():
    print('='*20 + 'FASE 2' + '='*20)
    sleep(1)
    quebra_linha()
    print(f'\n{personagem1} precisa escolher :\n\n 1- faz uma coisa '+ '    ' + ' 2- faz outra\n')

    escolha_fase2 = False
    while escolha_fase2 == False:
        obstaculo_fase2 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase2 == 1: 
            print_slow(f'\nQue pena...{personagem1} escorregou nas pedras e foi levada pela correnteza!\n\nFIM DE JOGO!')
            sys.exit()
            escolha_fase2 = True
        elif obstaculo_fase2 == 2:
            quebra_linha()
            print_slow('\nBoa escolha! Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_fase2 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase2 = False

def terceira_fase_jogador1():
    print('='*20 + 'FASE 3' + '='*20)
    sleep(1)
    quebra_linha()
    print(f'{personagem1} precisa escolher :\n\n 1- faz uma coisa '+ '    ' + ' 2- faz outra\n')

    escolha_fase3 = False
    while escolha_fase3 == False:
        obstaculo_fase3 = int(input('Digite a opção escolhida: '))
       
        if obstaculo_fase3 == 1: 
            print_slow(f'\nQue pena...{personagem1} escorregou nas pedras e foi levada pela correnteza!\n\n\FIM DE JOGO!')
            escolha_fase3 = True
        elif obstaculo_fase3 == 2:
            quebra_linha()
            print_slow('\nBoa escolha!Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_fase3 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase3 = False

def fase_final_jogador1():
    print('='*20 + 'FASE FINAL' + '='*20)
    sleep(1)
    quebra_linha()
    print(f'{personagem1} precisa escolher :\n\n 1- faz uma coisa'+ '    ' + '2- faz outra\n')

    escolha_final = False
    while escolha_final == False:
        obstaculo_final = int(input('Digite a opção escolhida: '))
       
        if obstaculo_final == 1: 
            print_slow(f'\nQue pena...{personagem1} escorregou nas pedras e foi levada pela correnteza!\n\nFIM DE JOGO!') 
            escolha_final = True
        elif obstaculo_final == 2:
            quebra_linha()
            print_slow('\nBoa escolha!Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_final = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_final = False


def primeira_fase_jogador2():
    print('='*20 + 'FASE 1' + '='*20)
    sleep(1)
    quebra_linha()
    print('Bem-vindo a Floresta de Tugah! Preparado para a aventura?\n\n')
    print(f'{personagem2} está a beira do rio, ela deve:\n\n 1- Ppppppp '+ '    ' + ' 2- nnnnnnnn\n')

    escolha_fase1 = False
    while escolha_fase1 == False:
        obstaculo_fase1 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase1 == 1: 
            print_slow(f'\nQue pena...{personagem2} escorregou nas pedras e foi levada pela correnteza!\n\nFIM DE JOGO!')
            
            escolha_fase1 = True
        elif obstaculo_fase1 == 2:
            quebra_linha()
            print_slow('\nBoa escolha!Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_fase1 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase1 = False

def segunda_fase_jogador2():
    print('='*20 + 'FASE 2' + '='*20)
    sleep(1)
    quebra_linha()
    print(f'\n{personagem2} precisa escolher :\n\n 1- faz uma coisa '+ '    ' + ' 2- faz outra\n')

    escolha_fase2 = False
    while escolha_fase2 == False:
        obstaculo_fase2 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase2 == 1: 
            print_slow(f'\nQue pena...{personagem2} escorregou nas pedras e foi levada pela correnteza!\n\nFIM DE JOGO!')
            escolha_fase2 = True
        elif obstaculo_fase2 == 2:
            quebra_linha()
            print_slow('\nBoa escolha! Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_fase2 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase2 = False

def terceira_fase_jogador2():
    print('='*20 + 'FASE 3' + '='*20)
    sleep(1)
    quebra_linha()
    print(f'{personagem2} precisa escolher :\n\n 1- faz uma coisa '+ '    ' + ' 2- faz outra\n')

    escolha_fase3 = False
    while escolha_fase3 == False:
        obstaculo_fase3 = int(input('Digite a opção escolhida: '))
       
        if obstaculo_fase3 == 1: 
            print_slow(f'\nQue pena...{personagem2} escorregou nas pedras e foi levada pela correnteza!\n\n\FIM DE JOGO!')
            escolha_fase3 = True
        elif obstaculo_fase3 == 2:
            quebra_linha()
            print_slow('\nBoa escolha!Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_fase3 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase3 = False

def fase_final_jogador2():
    print('='*20 + 'FASE FINAL' + '='*20)
    sleep(1)
    quebra_linha()
    print(f'{personagem2} precisa escolher :\n\n 1- faz uma coisa'+ '    ' + '2- faz outra\n')

    escolha_final = False
    while escolha_final == False:
        obstaculo_final = int(input('Digite a opção escolhida: '))
       
        if obstaculo_final == 1: 
            print_slow(f'\nQue pena...{personagem2} escorregou nas pedras e foi levada pela correnteza!\n\nFIM DE JOGO!') 
            sys,exit()
            escolha_final = True
        elif obstaculo_final == 2:
            quebra_linha()
            print_slow('\nBoa escolha!Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_final = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_final = False


def primeira_fase_jogador3():
    print('='*20 + 'FASE 1' + '='*20)
    sleep(1)
    quebra_linha()
    print('Bem-vindo a Floresta de Tugah! Preparado para a aventura?\n\n')
    print(f'{personagem3} está a beira do rio, ela deve:\n\n 1- Pular no rio '+ '    ' + ' 2- Usar uma corda\n')

    escolha_fase1 = False
    while escolha_fase1 == False:
        obstaculo_fase1 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase1 == 1: 
            print_slow(f'\nQue pena...{personagem3} escorregou nas pedras e foi levada pela correnteza!\n\nFIM DE JOGO!')
            escolha_fase1 = True
        elif obstaculo_fase1 == 2:
            quebra_linha()
            print_slow('\nBoa escolha!Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_fase1 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase1 = False

def segunda_fase_jogador3():
    print('='*20 + 'FASE 2' + '='*20)
    sleep(1)
    quebra_linha()
    print(f'\n{personagem3} precisa escolher :\n\n 1- faz uma coisa '+ '    ' + ' 2- faz outra\n')

    escolha_fase2 = False
    while escolha_fase2 == False:
        obstaculo_fase2 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase2 == 1: 
            print_slow(f'\nQue pena...{personagem3} escorregou nas pedras e foi levada pela correnteza!\n\nFIM DE JOGO!')
            escolha_fase2 = True
        elif obstaculo_fase2 == 2:
            quebra_linha()
            print_slow('\nBoa escolha! Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_fase2 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase2 = False

def terceira_fase_jogador3():
    print('='*20 + 'FASE 3' + '='*20)
    sleep(1)
    quebra_linha()
    print(f'{personagem3} precisa escolher :\n\n 1- faz uma coisa '+ '    ' + ' 2- faz outra\n')

    escolha_fase3 = False
    while escolha_fase3 == False:
        obstaculo_fase3 = int(input('Digite a opção escolhida: '))
       
        if obstaculo_fase3 == 1: 
            print_slow(f'\nQue pena...{personagem3} escorregou nas pedras e foi levada pela correnteza!\n\n\FIM DE JOGO!')
            escolha_fase3 = True
        elif obstaculo_fase3 == 2:
            quebra_linha()
            print_slow('\nBoa escolha!Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_fase3 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase3 = False

def fase_final_jogador3():
    print('='*20 + 'FASE FINAL' + '='*20)
    sleep(1)
    quebra_linha()
    print(f'{personagem3} precisa escolher :\n\n 1- faz uma coisa'+ '    ' + '2- faz outra\n')

    escolha_final = False
    while escolha_final == False:
        obstaculo_final = int(input('Digite a opção escolhida: '))
       
        if obstaculo_final == 1: 
            print_slow(f'\nQue pena...{personagem3} escorregou nas pedras e foi levada pela correnteza!\n\nFIM DE JOGO!') 
            escolha_final = True
        elif obstaculo_final == 2:
            quebra_linha()
            print_slow('\nBoa escolha!Continue assim e logo chegará ao tesouro!\n\n\n')
            escolha_final = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_final = False


quebra_linha()
print('BEM-VINDO AO JOGO CAÇA AO TESOURO!')#centralizar a frase
print('='*40)
print_slow('\nANNA, JONH E ANTONY ALÉM DE SEREM GRANDES AMIGOS TAMBÉM SÃO GRANDES AVENTUREIROS.\nDESSA VEZ ELES SE PREPARAM PARA UMA GRANDE EXPEDIÇÃO PELA FLORESTA DE TUGAH EM BUSCA DO TESOURO PERDIDO\nSERÁ QUE ELES CONSEGUIRÃO COMPLETAR MAIS ESSA MISSÂO?\n\n')
sleep(1)

  
print('OPÇÕES JOGADORES')
print('='*20)
print(f'[1]={personagem1}\n{descricao_personagem1}\n\n[2]={personagem2}\n{descricao_personagem2}\n\n[3]= {personagem3}\n{descricao_personagem3}') 
escolha_personagem()
print('LOADING....\n\n')
sleep(3)


if personagem == 1:    
   primeira_fase_jogador1()
   segunda_fase_jogador1()
   terceira_fase_jogador1()
   fase_final_jogador1()

elif personagem == 2:    
   primeira_fase_jogador2()
   segunda_fase_jogador2()
   terceira_fase_jogador2()
   fase_final_jogador2()

elif personagem == 3:    
   primeira_fase_jogador3()
   segunda_fase_jogador3()
   terceira_fase_jogador3()
   fase_final_jogador3()



# retornar_jogo = False
# def reiniciar_jogo():
#     jogar_novamente = input('Deseja jogar novamente?[S / N] ').upper()
#     while retornar_jogo == False:    
#         if jogar_novamente= 'S':
#             retornar_jogo = True
#         elif jogar_novamente = 'N':
#             print('Até logo!')
#             retornar_jogo = True
#         else:
#             print('Digite uma opção válida. S ou N')
#             retornar_jogo = False
    