from time import sleep
import sys


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.02)

def quebra_linha():                                                     
    print(''*50) 
  
personagem1 = 'ANNA'
personagem2 = 'JOHN'
personagem3 = 'ANTONY'
 
# descricao_personagem1 = '\nCORAJOSA, LIDERA A MAIORIA DAS AVENTURAS E ADORA RESOLVER ENIGMAS.\nSEU PONTO FRACO:NÃO SABER NADAR.\n'
# descricao_personagem2 = '\nEXPLORADOR NATO, SEMPRE EM BUSCA DE UMA AVENTURA NÃO MEDE ESFORÇOS PARA CONSEGUIR CONQUISTAR SEUS OBJETIVOS.\nSEU PONTO FRANCO: A TEIMOSIA.\n'
# descricao_personagem3 = '\nARQUEÓLOGO,APAIXONADO POR LENDAS DE TESOUROS, É O MAIS ORGANIZADO DO GRUPO.NÃO DÁ UM PASSO SEM ANALISAR TODA SITUAÇÃO EM SUA VOLTA.\nSEU PONTO FRACO:TEM MEDO DE ALTURA.\n'



def escolha_personagem():
    global personagem
    opcao_valida = False

    while opcao_valida == False:
        personagem = int(input('\nESCOLHA SEU JOGADOR: '))
       
        if personagem == 1:
            quebra_linha()
            print_slow(str(f'Você escolheu a {personagem1}.'))
            quebra_linha()
            opcao_valida = True
        elif personagem == 2:
            quebra_linha()
            print_slow(str(f'Você escolheu a {personagem2}.'))
            quebra_linha()
            opcao_valida =True
        elif personagem == 3:
            quebra_linha()
            print_slow(str(f'Você escolheu a {personagem3}.'))
            quebra_linha()
            opcao_valida = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1, 2 OU 3\n')
            quebra_linha()
            opcao_valida = False

    return personagem


def primeira_fase_jogador1():
    print('='*52 + 'FASE 1' + '='*52) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Você está na entrada da floresta e há duas trilhas à sua frente.A da direita, que tem uma bela vista para montanhas e um lago lindo! A mata é aberta, assim o caminho está bem\niluminado.E tem a da esquerda, que mesmo durante o dia é bem escura, já que a mata é densa. Você não consegue enxergar até onde vai o final daquela trilha, nem se há um fim de fato.\n\nQual você escolhe seguir?\n\n 1- Esquerda '+ '    ' + ' 2- Direita\n')

    escolha_fase1 = False
    while escolha_fase1 == False:
        obstaculo_fase1 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase1 == 1: 
            print_slow('Você começa a andar pela trilha e sente que pisou em algo. Você olha para baixo e vê que acabou pisando em uma planta com espinhos venenosos e você acaba morrendo em poucos segundos.\nFIM DE JOGO!')
            sys.exit()
            # escolha_fase1 = True
        elif obstaculo_fase1 == 2:
            quebra_linha()
            print_slow('\nBom começo! Você continua seguindo e está tudo bem! Parabéns, parece que você encontrou o caminho certo!\n\n\n')
            escolha_fase1 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase1 = False

def segunda_fase_jogador1():
    print('='*52 + 'FASE 2' + '='*52) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Seguindo pela mata densa você dá de cara com um javali selvagem! E você está com fome. Mais a frente há um arbusto com frutinhas coloridas.\n\nO que você faz?\n\n 1- Você come as frutinhas '+ '    ' + ' 2- Você resolve atacar o javali com sua faca.\n')

    escolha_fase2 = False
    while escolha_fase2 == False:
        obstaculo_fase2 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase2 == 1:
            quebra_linha() 
            print_slow('HUuummmm...você escolheu bem demais!!! Frutinhas deliciosas! Está tudo certo e o javali já foi embora também.\n\n\n')
            quebra_linha()
            escolha_fase2 = True
        elif obstaculo_fase2 == 2:
            quebra_linha()
            print_slow('Você resolve atacar o javali com sua faca. Você não é mais rápido que ele. E ele te ataca de volta! Sua presa perfura seu peito e você morreu!\nFIM DE JOGO!')
            sys.exit()
            escolha_fase2 = True 
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase2 = False

def terceira_fase_jogador1():
    print('='*52 + 'FASE 3' + '='*52) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Você anda mais um pouco e sem querer acaba pisando em uma pedra pontiaguda. Seu pé está sangrando bastante e sujo.\nO que você faz para tratar a ferida?\n\n 1- Você tira a camisa para estancar o sangue '+ '    ' + ' 2- Você passa uma pomada que encontrou na mochila\n')

    escolha_fase3 = False
    while escolha_fase3 == False:
        obstaculo_fase3 = int(input('Digite a opção escolhida: '))
        
        if obstaculo_fase3 == 1: 
            print_slow('Após estancar o sangue, você consegue caminhar até um riacho e lavar o pé.Por sorte o corte não foi profundo e você segue em busca do Tesouro.\n\n\n')
            quebra_linha()           
            escolha_fase3 = True
        elif obstaculo_fase3 == 2:
            quebra_linha()
            print_slow('Você caminha mais um pouco mas vê que a pomada não resolveu o problema por conta da sujeira e terra que acumulou na ferida.Seu pé infeccionou e você não consegue mais seguir em frente.\nFIM DE JOGO!\n\n\n')
            sys.exit()
            escolha_fase3 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase3 = False

def fase_final_jogador1():
    print('='*50 + 'FASE FINAL' + '='*50) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Você finalmente chega a caverna onde está o Tesouro e gora você precisa enfrentar o Guardião.Ele está vindo em sua direção pronto para te atacar. Como você se defende?\n\n 1- Você parte pra cima dele com a sua faca'+ '    ' + '2- Você lança pedras nele\n')

    escolha_final = False
    while escolha_final == False:
        obstaculo_final = int(input('Digite a opção escolhida: '))
       
        if obstaculo_final == 2: 
            print('Antes que o Guardião chegue até você, você arremessa pedras  e uma acaba acertando a cabeça dele.Você aproveita o momento de distração dele e o acerta com a faca.\n\nVOCÊ VENCEU!!!\n\nPARABÉNS, O TESOURO AGORA É TODO SEU!')        
            escolha_final = True
        elif obstaculo_final == 1:
            quebra_linha()
            print_slow('O Guardião acerta sua cabeça com um pedaço de pau e você acaba caindo no chão sem chances de defesa. Ele consegue pegar a faca da sua mão e te mata.VOCÊ PERDEU!\n\n\nFIM DE JOGO.\n\n\n')
            escolha_final = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_final = False


def primeira_fase_jogador2():
    print('='*52 + 'FASE 1' + '='*52) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Você se encontra de pé, no meio do deserto. Você mexe em seus bolsos e não sente nada neles. Olha ao redor e apenas vê as montanhas de areia que te cercam e o forte Sol.Olha para frente e para trás sem saber ao certo para onde deve seguir.:\n\n 1- Segue para frente '+ '    ' + ' 2- Segue para trás\n')

    escolha_fase1 = False
    while escolha_fase1 == False:
        obstaculo_fase1 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase1 == 1: 
            print_slow('\nVocê caminha por alguns minutos, que se tornam, horas e além de exausto,agora está perdido. Sem comida, sem água e um forte calor te artomentando você cai no chão desmaiado e não consegue mais continuar.\n FIM DE JOGO')
            sys.exit()
            escolha_fase1 = True
        elif obstaculo_fase1 == 2:
            quebra_linha()
            print_slow('Ao caminhar por alguns minutos você encontra um cacto que pode servir como ponto de referencia.\n\n\n')
            escolha_fase1 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase1 = False

def segunda_fase_jogador2():
    print('='*52 + 'FASE 2' + '='*52) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Você está com sede e olha para o cacto e se lembra que pode retirar água dele e se hidratar.\n\n 1- Não tenta como medo de se machucar com os espinhos '+ '    ' + ' 2- Abre o cacto \n')

    escolha_fase2 = False
    while escolha_fase2 == False:
        obstaculo_fase2 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase2 == 1: 
            print_slow('Segue por mais alguns metros, mas não aguenta mais e acaba morrendo de desidratação. Tarde demais para voltar atrás do cacto.\n\nFIM DE JOGO!')
            sys.exit()
            escolha_fase2 = True
        elif obstaculo_fase2 == 2:
            quebra_linha()
            print_slow('\nMesmo sem saber direito como fazer, ainda assim você consegue pegar bastante liquido. Voce se hidrata bastante e segue caminho.\n\n\n')
            escolha_fase2 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase2 = False

def terceira_fase_jogador2():
    print('='*52 + 'FASE 3' + '='*52) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Seguindo mais um pouco você vê algo se mexendo na areia mas não tem certeza do que é, mas acredita ser algum animalzinho que seria ideal para uma refeição.\n\n 1- Você vai atrás para tentar caçar '+ '    ' + ' 2- Não vai atrás e segue caminho\n')

    escolha_fase3 = False
    while escolha_fase3 == False:
        obstaculo_fase3 = int(input('Digite a opção escolhida: '))
       
        if obstaculo_fase3 == 1: 
            print_slow(f'\nQue pena...{personagem2} escorregou nas pedras e foi levada pela correnteza!\n\n\FIM DE JOGO!')
            sys.exit()
            escolha_fase3 = True
        elif obstaculo_fase3 == 2:
            quebra_linha()
            print_slow('você continua andando e ao olhar para trás percebe que era uma cobra naja. Nossa! foi por pouco! Você continua em busca do Tesouro.\n\n\n')
            escolha_fase3 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase3 = False

def fase_final_jogador2():
    print('='*50 + 'FASE FINAL' + '='*50) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Após caminhar mais um pouco você avista a piramide aonde está o tesouro, segue até ela e vê a entrada aberta. Ao entrar é supreendido por uma mulher alta e enfaixada. Uma múmia! Atrás dela você vê um facão no chão, provavelmente de outro explorador que tentou passsar ali antes de você.\nComo você resolve passar pela guardiã?\n\n 1- Tenta passar correndo e alcançar o falcão'+ '    ' + '2- Tenta lutar com ela\n')

    escolha_final = False
    while escolha_final == False:
        obstaculo_final = int(input('Digite a opção escolhida: '))
       
        if obstaculo_final == 1: 
            print_slow('O primeiro golpe que você tenta acertar e ela te agarra e te morde. Você não resiste e acaba morrendo ali.\n VOCÊ PERDEU!\n FIM DE JOGO!\n\n')            
            escolha_final = True
        elif obstaculo_final == 2:
            quebra_linha()
            print_slow('\nVocê consegue passar por ela correndo facilmente,alcança o facão e desfere um golpe certeiro matando -a.\n\nVocê conseguiu! Parabéns, o Tesouro é seu!\n\n\n')
            escolha_final = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_final = False


def primeira_fase_jogador3():
    print('='*52 + 'FASE 1' + '='*52) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Após um acidente com o seu barco,você está à deriva em um bote salva-vidas. No bote você encontra um balde e um pedaço de madeira. Ao seu redor há um inifinito de oceano e você avista lá longe a ilha do tesouro.\n\n 1- Você pula do bote e resolve ir nadando '+ '    ' + ' 2- Você resolver ir remando com o bote\n')

    escolha_fase1 = False
    while escolha_fase1 == False:
        obstaculo_fase1 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase1 == 1: 
            print_slow('Após decidir que nadar seria mais rápido do que tentar remar com bote, você começa sua jornada e no meio do caminho você vê um onda vindo de longe e te levando para o fundo assim que ela termina, quando você finalmente consegue voltar a superficie, outra onda te atinge, você começa a se afogar e morre.\n FIM DE JOGO\n\n')
            sys.exit()
            escolha_fase1 = True
        elif obstaculo_fase1 == 2:
            quebra_linha()
            print_slow('\n Após muito esforço e utilizando a madeira você começa a sair do lugar, não consegue ir exatamente reto em direção da ilha, o que é até bom, já que assim acaba desviando de onde as ondas estão quebrando e chega seguro á ilha.\n\n\n')
            escolha_fase1 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase1 = False

def segunda_fase_jogador3():
    print('='*52 + 'FASE 2' + '='*52) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Chegando na ilha você vê apenas um coqueiro e um buraco perto dele, chegando mais perto percebe que é uma entrada subterrânea para algum lugar.\n\n 1- Você decide entrar '+ '    ' + ' 2- Você ignora a entrada e segue pela praia\n')

    escolha_fase2 = False
    while escolha_fase2 == False:
        obstaculo_fase2 = int(input('Digite a opção escolhida: '))

        if obstaculo_fase2 == 1: 
            print_slow('Assim que você entra, a entrada se fecha com areia e tudo começa a desabar, você é soterrado por muita areia e nao consegue se mexer e vai perdendo o ar até que, enfim, morre.\n\nFIM DE JOGO!')
            sys.exit()
            escolha_fase2 = True
        elif obstaculo_fase2 == 2:
            quebra_linha()
            print_slow('\nApós alguns minutos de caminhada, você ouve um forte barulho e olha para trás, a entrada já não está mais lá, vocÊ segue em frente\n\n\n')
            escolha_fase2 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase2 = False

def terceira_fase_jogador3():
    print('='*52 + 'FASE 3' + '='*52) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Após alguns minutos de caminhada, com seu pedaço  de madeira e o balde, você avista um cadurme de peixes por perto da praia. Mais a frente tem uma arvore com alguns frutos. E você está com fome.\n\n 1- Você decide escalar a àrvore para pegar os frutos '+ '    ' + ' 2- Você resolve ir pescarn')

    escolha_fase3 = False
    while escolha_fase3 == False:
        obstaculo_fase3 = int(input('Digite a opção escolhida: '))
       
        if obstaculo_fase3 == 1: 
            print_slow('Você sobe numa pedra para pegar altura e alcançar os galhos, você se pendura e quando consegue subir o galho em que você está quebra e você cai de cabeça na pedra. Você morre na hora.\n\n\FIM DE JOGO!')
            sys.exit()
            escolha_fase3 = True
        elif obstaculo_fase3 == 2:
            quebra_linha()
            print_slow('\nChegando perto você consegue fazer um tipo de cesta com o pedaço de madeira e o balde, amarrando com sua camisa. E consegue pegar alguns dos peixes e se alimentar, para seguir em frente.\n\n\n')
            escolha_fase3 = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_fase3 = False

def fase_final_jogador3():
    print('='*50 + 'FASE FINAL' + '='*50) 
    print('='*110)
    quebra_linha() 
    sleep(1)
    quebra_linha()
    print('Após se alimentar, você se desfaz do balde e fica apenas com o pedaço de madeira, andando por mais alguns metros você ve uma cabana supensa no mar, não muito longe da faixa de areia. Você percebe que há alguns tubarões guardando o acesso para a cabana. Os guardiões do tesouro!\n\n 1- Você volta até o bote e tenta atravessar até lá com ele'+ '    ' + '2- faz outra\n')

    escolha_final = False
    while escolha_final == False:
        obstaculo_final = int(input('Digite a opção escolhida: '))
        
        if obstaculo_final == 1: 
            print_slow('Assim que você chega perto da area dos tubarôes, eles não exitam e já atacam o bote, você é devorado vivo\n\nVOCÊ PERDEU!\n\nFIM DE JOGO!')
            escolha_final = True
        elif obstaculo_final == 2:
            quebra_linha()
            print_slow('\nvocê volta até o balde e encontra uns pedaços dos peixes que você comeu há pouco e joga ao mar e vê todos os tubarões indo atrás para pegar e começam a brigar entre si. Você consegue passar nadando facilmente já que estão distraidos. Você chega à cabana encontra um baú onde está o tesouro. Parabens! Ele é todo seu.\n\n\n')
            escolha_final = True
        else:
            opcao_invalida = print('\nOPÇÃO INVÁLIDA. DIGITE 1 ou 2\n')
            escolha_final = False


quebra_linha()
print('='*39 + 'BEM VINDO AO JOGO CAÇA AO TESOURO' + '='*38) 
print('='*110)
print_slow('\nANNA, JONH E ANTONY ALÉM DE SEREM GRANDES AMIGOS E ADORAM UMA AVENTURA.\nDESSA VEZ ELES SE PREPARAM PARA ENFRENTAR OS PERIGOS DE IR EM BUSCA DE UM TESOURO PERDIDO.\nSERÁ QUE ELES CONSEGUIRÃO COMPLETAR MAIS ESSA MISSÂO?\n\n')
sleep(1)

  
print('='*51 + 'JOGADORES' + '='*50) 
print('='*110)
quebra_linha() 
print_slow(f'[1]={personagem1}\n')
# print(f'{descricao_personagem1}\n\n')
sleep(1)
print_slow(f'[2]={personagem2}\n')
# print(f'{descricao_personagem2}\n\n')
sleep(1)
print_slow(f'[3]={personagem3}\n')
# print(f'{descricao_personagem1}\n\n')
sleep(1)
escolha_personagem()
quebra_linha()
print_slow('VAMOS COMEÇAR NOSSA AVENTURA? O OBJETIVO É SIMPLES: BASTA SOBREVIVER E ACHAR O TESOURO! SERÁ QUE VAI SER TÃO SIMPLES ASSIM?\n\nCHEGA DE ENROLAÇÃO E VAMOS LÁ!\n\n')
sleep(1)



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
#     jogar_novamente = input('Deseja jogar novamente?[S / N] ')  #incluir upper
#     while retornar_jogo == False:    
#         if jogar_novamente.upper()== 'S':
#             retornar_jogo = True
#         elif jogar_novamente.upper() == 'N':
#             print('Até logo!')
#             retornar_jogo = True
#         else:
#             print('Digite uma opção válida. S ou N')
#             retornar_jogo = False
    