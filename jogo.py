import funcoes
import base_questoes
jogo = True
ajudas = 2
pulos = 3
questoes = 1
questoes_corretas = 0
lista_premios = [1000,5000,10000,30000,50000,100000,300000,500000,1000000]
lista_possiveis_respostas = ['A','B','C','D']
print('\33[1;33mBem vindo ao jogo da Fortuna! Aqui terá a oportunidade de enriquecer!!\33[m')
nome_do_jogador = input('Qual seu nome?')
print(f'\33[1;37mBem vindo {nome_do_jogador}, você tem direito a 3 pulos e 2 ajudas.')
print(f'\33[1;34mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"\33[m')
preparado = input('Você esta preparado(a)? [sim/nao]')
if preparado == 'sim':
    jogo = True
    print('Então vamos começar! Boa sorte!')
else:
    print('Tudo bem, até a proxima!')
base_de_questoes = base_questoes.quest
base_de_questoes_correta = funcoes.transforma_base(base_de_questoes)
questoes_ja_sorteadas = []
while jogo == True:
    if questoes <= 3:
        nivel = 'facil'
    elif 3 < questoes<= 6:
        nivel = 'medio'
    else:
        nivel = 'dificil'
    if questoes == 1:
        print('Vamos começar com questões de nível fácil!')
    if questoes==4:
        print('Está indo bem, vamos aumentar o nível das questões agora!')
    if questoes == 7:
        print('Uau! Você é bom, mas agora chegam as questões difíceis!')
    lista_para_validar = base_de_questoes_correta[nivel]
    lista_validadas = funcoes.valida_questoes(lista_para_validar)
    lista_questoes_validas = []
    for i in range(0,len(lista_validadas)):
        if lista_validadas[i] == {}:
            lista_questoes_validas.append(lista_para_validar[i])
    base_de_questoes_correta[nivel] = lista_questoes_validas
    questao_sorteada = funcoes.sorteia_questao_inedida(base_de_questoes_correta,nivel,questoes_ja_sorteadas)
    questoes_ja_sorteadas.append(questao_sorteada)
    print(funcoes.questao_para_texto(questao_sorteada,questoes))
    resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
    while resposta != 'A' and resposta != 'B' and resposta !="C" and resposta != 'D' and resposta != 'ajuda' and resposta != 'pular':
        print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"')
        print(funcoes.questao_para_texto(questao_sorteada,questoes))
        resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')    
    if resposta == questao_sorteada['correta']:
        questoes_corretas +=1
        questoes+=1
        print(f'Parabens! Você acertou! Seu prêmio atual é de R$: {lista_premios[questoes_corretas]:.2f}')
        continuar = input('Deseja continuar? [sim/nao]')
        if continuar == 'nao':
            print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
            jogo = False
    elif resposta == 'pular':
        if pulos > 0:
            questoes_corretas+=1
            questoes+=1
            pulos = pulos-1
            print(f'Agora Possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
            continuar = input('Deseja continuar? [sim/nao]')
            if continuar == 'nao':
                print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                jogo = False
        else:
            print('Voce não possui mais pulos!')
            print(funcoes.questao_para_texto(questao_sorteada,questoes))
            resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
            
            while resposta == 'pular':
                print('Voce não possui mais pulos!')
                print(funcoes.questao_para_texto(questao_sorteada,questoes))
                resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
                
            if resposta == questao_sorteada['correta']:
                questoes_corretas +=1
                questoes+=1
                print(f'Parabens! Você acertou! Já possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
                continuar = input('Deseja continuar? [sim/nao]')
                if continuar == 'nao':
                    print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                    jogo = False
            elif resposta in lista_possiveis_respostas and resposta!= questao_sorteada['correta']:
                print('Você errou! Que pena... mais sorte da proxima vez')
                jogo = False
            elif resposta == 'ajuda':
                if ajudas > 0:
                    ajudas = ajudas -1
                    print(funcoes.gera_ajuda(questao_sorteada))
                    resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
                    if resposta == questao_sorteada['correta']:
                        questoes_corretas +=1
                        questoes+=1
                        print(f'Parabens! Você acertou! Já possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
                        continuar = input('Deseja continuar? [sim/nao]')
                        if continuar == 'nao':
                            print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                            jogo = False
                    else:
                        print('Você errou! Que pena... mais sorte da proxima vez')
                        jogo = False
                else: 
                    print('Você não possui mais ajudas!')
                    print(funcoes.questao_para_texto(questao_sorteada,questoes))
                    resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas')
                    
                    while resposta == 'ajuda':
                        print('Você não possui mais ajudas!')
                        print(funcoes.questao_para_texto(questao_sorteada,questoes))
                        resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas')
                    if resposta == questao_sorteada['correta']:
                        questoes_corretas +=1
                        questoes+=1
                        print(f'Parabens! Você acertou! Já possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
                        continuar = input('Deseja continuar? [sim/nao]')
                        if continuar == 'nao':
                            print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                            jogo = False
                    else:
                        print('Você errou! Que pena... mais sorte da proxima vez')
                        jogo = False
    elif resposta == 'ajuda':
        if ajudas > 0:
            ajudas = ajudas -1
            print(funcoes.gera_ajuda(questao_sorteada))
            resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
            while resposta == 'ajuda':
                print('Você ja pediu ajuda nesta questão')
                resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
            if resposta == questao_sorteada['correta']:
                questoes_corretas +=1
                questoes+=1
                print(f'Parabens! Você acertou! Já possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
                continuar = input('Deseja continuar? [sim/nao]')
                if continuar == 'nao':
                    print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                    jogo = False
            elif resposta in lista_possiveis_respostas and resposta!= questao_sorteada['correta']:
                print('Você errou! Que pena... mais sorte da proxima vez')
                jogo = False
            elif resposta == 'pular':
                if pulos > 0:
                    questoes_corretas+=1
                    questoes+=1
                    pulos = pulos-1
                    print(f'Agora Possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
                    continuar = input('Deseja continuar? [sim/nao]')
                    if continuar == 'nao':
                        print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                        jogo = False
                else:
                    print('Voce não possui mais pulos!')
                    print(funcoes.questao_para_texto(questao_sorteada,questoes))
                    resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
                while resposta == 'pular':
                    print('Voce não possui mais pulos!')
                    print(funcoes.questao_para_texto(questao_sorteada,questoes))
                    resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
                if resposta == questao_sorteada['correta']:
                    questoes_corretas +=1
                    questoes+=1
                    print(f'Parabens! Você acertou! Já possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
                    continuar = input('Deseja continuar? [sim/nao]')
                    if continuar == 'nao':
                        print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                        jogo = False
        else: 
            print('Você não possui mais ajudas!')
            print(funcoes.questao_para_texto(questao_sorteada,questoes))
            resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas')       
            while resposta == 'ajuda':
                print('Você não possui mais ajudas!')
                print(funcoes.questao_para_texto(questao_sorteada,questoes))
                resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas')
            if resposta == questao_sorteada['correta']:
                questoes_corretas +=1
                questoes+=1
                print(f'Parabens! Você acertou! Já possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
                continuar = input('Deseja continuar? [sim/nao]')
                if continuar == 'nao':
                    print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                    jogo = False
            elif resposta in lista_possiveis_respostas and resposta!= questao_sorteada['correta']:
                print('Você errou! Que pena... mais sorte da proxima vez')
                jogo = False
            elif resposta == 'pular':
                if pulos > 0:
                    questoes_corretas+=1
                    questoes+=1
                    pulos = pulos-1
                    print(f'Agora Possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
                    continuar = input('Deseja continuar? [sim/nao]')
                    if continuar == 'nao':
                        print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                        jogo = False
                else:
                    print('Voce não possui mais pulos!')
                    print(funcoes.questao_para_texto(questao_sorteada,questoes))
                    resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
                while resposta == 'pular':
                    print('Voce não possui mais pulos!')
                    print(funcoes.questao_para_texto(questao_sorteada,questoes))
                    resposta = input(f'Qual sua resposta? Você possui {pulos} pulos e {ajudas} ajudas:')
                if resposta == questao_sorteada['correta']:
                    questoes_corretas +=1
                    questoes+=1
                    print(f'Parabens! Você acertou! Já possui um premio de R$:{lista_premios[questoes_corretas]:.2f}')
                    continuar = input('Deseja continuar? [sim/nao]')
                    if continuar == 'nao':
                        print(f'Parabens! Você saiu com um total de R$:{lista_premios[questoes_corretas]:.2f}')
                        jogo = False
                elif resposta in lista_possiveis_respostas and resposta!= questao_sorteada['correta']:
                    print('Você errou! Que pena... mais sorte da proxima vez')
                    jogo = False
    if questoes == 9:
        print('Parabens!!!')
        print(f'Você ganhou o jogo da Fortuna e volta para a casa com um valor de R$: {lista_premios[questoes_corretas]:.2f}')
        print('Muito Bem! Até a proxima')
        jogo = False