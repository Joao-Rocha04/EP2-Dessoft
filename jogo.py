jogar_novamente = True
import funcoes
import base_questoes
while jogar_novamente == True:
    jogo = True
    ajudas = 2
    pulos = 3
    questoes = 1
    questoes_corretas = 0
    lista_premios = [1000,5000,10000,30000,50000,100000,300000,500000,1000000]
    lista_possiveis_respostas = ['A','B','C','D']
    lista_todas_possiveis = ['A','B','C','D','pula','ajuda','parar']
    print('\33[1;33mBem vindo ao jogo da Fortuna! Aqui terá a oportunidade de enriquecer!!\33[m')
    nome_do_jogador = input('Qual seu nome?')
    print(f'\33[1;37mBem vindo {nome_do_jogador}, você tem direito a 3 pulos e 2 ajudas.')
    print(f'\33[1;34mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"\33[m')
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
        y = True
        while y == True:
            print(funcoes.questao_para_texto(questao_sorteada,questoes))
            resposta = input(f'Qual sua resposta?')
            if resposta not in lista_todas_possiveis:
                print('Opção Inválida!')
                print(f'\33[1;34mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"\33[m')
                resposta = input(f'Qual sua resposta?')
            elif resposta == questao_sorteada['correta']:
                questoes+=1
                questoes_corretas +=1
                print(f'Você acertou! Seu premio agora é de R$: {lista_premios[questoes_corretas]:.2f}')
                y = False
            elif resposta == 'pula':
                if pulos > 0:
                    pulos = pulos - 1
                    questoes+=1
                    questoes_corretas += 1
                    if pulos >0:
                        print(f'Ok, pulando! Você ainda tem {pulos} pulos')
                    else:
                        print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
                    y = False
                else:
                    print('Não deu! Você não tem mais direito a pulos')
                    y = True
            elif resposta == 'ajuda':
                if ajudas>0:
                    ajudas = ajudas -1
                    print(f'Ok, lá vem sua ajuda! Você ainda tem {ajudas} ajudas')
                    print(funcoes.gera_ajuda(questao_sorteada))
                    x = True
                    while x == True:
                        print(funcoes.questao_para_texto(questao_sorteada,questoes))
                        resposta = input(f'Qual sua resposta?')
                        if resposta not in lista_todas_possiveis:
                            print('Opção Inválida!')
                            print(f'\33[1;34mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"\33[m')
                            resposta = input(f'Qual sua resposta?')
                        elif resposta == 'ajuda':
                            print('Não deu! Você ja pediu ajuda nessa questao')
                            x = True
                        elif resposta == 'pula' and pulos > 0:
                            pulos = pulos -1
                            questoes+=1
                            questoes_corretas += 1
                            if pulos >0:
                                print(f'Ok, pulando! Você ainda tem {pulos} pulos')
                            else:
                                print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
                            y = False
                            x = False
                        elif resposta == 'pula' and pulos == 0:
                            print('Não deu! Você não tem mais direito a pulos')
                            x = True
                        elif resposta == questao_sorteada['correta']:
                            questoes+=1
                            questoes_corretas += 1
                            print(f'Você acertou! Seu premio agora é de R$: {lista_premios[questoes_corretas]:.2f}')
                            x = False
                            y = False
                        elif resposta in lista_possiveis_respostas and resposta!= questao_sorteada['correta']:
                            print('Que pena! Você errou e vai sair sem nada')
                            y = False
                            jogo = False
                        elif resposta == 'parar':
                            parar = input(f'Deseja mesmo parar [S/N] Se parar irá sairá com R$: {lista_premios[questoes_corretas]:.2f}')
                            if parar == 'S':
                                x = False
                                y = False
                                jogo = False
                            else:
                                x = True
                else:
                    print('Não deu! Você não tem mais direito a ajuda')
                    y = True
            elif resposta == 'parar':
                parar = input(f'Deseja mesmo parar [S/N] Se parar irá sairá com R$: {lista_premios[questoes_corretas]:.2f}')
                if parar == 'S':
                    y = False
                    jogo = False
                else:
                    y = True
            elif resposta in lista_possiveis_respostas and resposta!= questao_sorteada['correta']:
                print('Que pena! Você errou e vai sair sem nada')
                y = False
                jogo = False
    if questoes_corretas == 8:
        print('PARABÉNS, você zerou o jogo e ganhou 1 milhão de reais!!!')
        quer_jogar_novamente = input('Deseja jogar novamente [S/N]?')
        if quer_jogar_novamente == 'S':
            jogar_novamente = True
        else:
            jogar_novamente = False
    else:
        quer_jogar_novamente = input('Deseja jogar novamente [S/N]?')
        if quer_jogar_novamente == 'S':
            jogar_novamente = True
        else:
            jogar_novamente = False