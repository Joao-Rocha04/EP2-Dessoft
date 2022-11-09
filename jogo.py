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
    base_de_questoes = base_questoes.quest
    base_de_questoes_correta = funcoes.transforma_base(base_de_questoes)
    questoes_ja_sorteadas = []
    lista_nivel = ['facil','medio','dificil']
    x = True
    for nivel in lista_nivel:
        lista_para_validar = base_de_questoes_correta[nivel]
        lista_validadas = funcoes.valida_questoes(lista_para_validar)
        for i in range(0,len(lista_validadas)):
            if lista_validadas[i] != {}:
                print(f'\33[1;31mErro na base de questoes!!!\33[m')
                jogo = False
                x = False
    if x == True:
        print('\33[1;33mBem vindo ao jogo da Fortuna! Aqui terá a oportunidade de enriquecer!!\33[m\n')
        nome_do_jogador = input('Qual seu nome?')
        print(f'Bem vindo {nome_do_jogador}, você tem direito a 3 pulos e 2 ajudas.\n')
        print(f'\33[1;34mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"\33[m\n')
    while jogo == True:
        y = True
        if questoes <= 3:
            nivel = 'facil'
        elif 3 < questoes<= 6:
            nivel = 'medio'
        else:
            nivel = 'dificil'
        if questoes == 1:
            print('\33[1;36mVamos começar com questões de nível\33[m \33[1;32mfácil!\33[m\n')
        if questoes==4:
            print('\33[1;36mEstá indo bem, vamos aumentar o nível das questões para\33[m \33[1;33mmédio!\33[m\n')
        if questoes == 7:
            print('\33[1;36mUau! Você é bom, mas agora chegam as questões\33[m \33[1;31mdifíceis!\33[m\n')
        questao_sorteada = funcoes.sorteia_questao_inedida(base_de_questoes_correta,nivel,questoes_ja_sorteadas)
        questoes_ja_sorteadas.append(questao_sorteada)
        while y == True:
            print(funcoes.questao_para_texto(questao_sorteada,questoes))
            resposta = input(f'Qual sua resposta?')
            if resposta not in lista_todas_possiveis:
                print('\33[1;31mOpção Inválida!\33[m\n')
                print(f'\33[1;34mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"\33[m\n')
                y = True
            elif resposta == questao_sorteada['correta']:
                questoes+=1
                questoes_corretas +=1
                print(f'\33[1;32mVocê acertou! Seu premio agora é de R$: {lista_premios[questoes_corretas]:.2f}\33[m\n')
                y = False
            elif resposta == 'pula':
                if pulos > 0:
                    pulos = pulos - 1
                    questoes+=1
                    questoes_corretas += 1
                    if pulos >0:
                        print(f'\nOk, pulando! Você ainda tem {pulos} pulos\n')
                    else:
                        print('\nOk, pulando! ATENÇÃO: Você não tem mais direito a pulos!\n')
                    y = False
                else:
                    print('\33[1;31mNão deu! Você não tem mais direito a pulos\33[m\n')
                    y = True
            elif resposta == 'ajuda':
                if ajudas>0:
                    ajudas = ajudas -1
                    print(f'\nOk, lá vem sua ajuda! Você ainda tem {ajudas} ajudas\n')
                    print(funcoes.gera_ajuda(questao_sorteada))
                    x = True
                    while x == True:
                        print(funcoes.questao_para_texto(questao_sorteada,questoes))
                        resposta = input(f'Qual sua resposta?')
                        if resposta not in lista_todas_possiveis:
                            print('\33[1;31mOpção Inválida!\33[m\n')
                            print(f'\33[1;34mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"\33[m\n')
                            resposta = input(f'Qual sua resposta?')
                        elif resposta == 'ajuda':
                            print('\33[1;31mNão deu! Você ja pediu ajuda nessa questao\33[m\n')
                            x = True
                        elif resposta == 'pula' and pulos > 0:
                            pulos = pulos -1
                            questoes+=1
                            questoes_corretas += 1
                            if pulos >0:
                                print(f'\nOk, pulando! Você ainda tem {pulos} pulos\n')
                            else:
                                print('\nOk, pulando! ATENÇÃO: Você não tem mais direito a pulos!\n')
                            y = False
                            x = False
                        elif resposta == 'pula' and pulos == 0:
                            print('\33[1;31mNão deu! Você não tem mais direito a pulos\33[m\n')
                            x = True
                        elif resposta == questao_sorteada['correta']:
                            questoes+=1
                            questoes_corretas += 1
                            print(f'\33[1;32mVocê acertou! Seu premio agora é de R$: {lista_premios[questoes_corretas]:.2f}\33[m\n')
                            x = False
                            y = False
                        elif resposta in lista_possiveis_respostas and resposta!= questao_sorteada['correta']:
                            print('\nQue pena! Você errou e vai sair sem nada\n')
                            x = False
                            y = False
                            jogo = False
                        elif resposta == 'parar':
                            parar = input(f'Deseja mesmo parar [S/N] Se parar irá sairá com R$: {lista_premios[questoes_corretas]:.2f}\n')
                            if parar == 'S':
                                print(f'\33[1;32mOk, você parou e seu premio é de R$: {lista_premios[questoes_corretas]:.2f}\33[m\n')
                                x = False
                                y = False
                                jogo = False
                            else:
                                x = True
                else:
                    print('\n\33[1;31mNão deu! Você não tem mais direito a ajuda\33[m\n')
                    y = True
            elif resposta == 'parar':
                parar = input(f'Deseja mesmo parar [S/N] Se parar irá sairá com R$: {lista_premios[questoes_corretas]:.2f}\n')
                if parar == 'S':
                    print(f'\33[1;32mOk, você parou e seu premio é de R$: {lista_premios[questoes_corretas]:.2f}\33[m\n')
                    y = False
                    jogo = False
                else:
                    y = True
            elif resposta in lista_possiveis_respostas and resposta!= questao_sorteada['correta']:
                print('\nQue pena! Você errou e vai sair sem nada\n')
                y = False
                jogo = False
    if questoes_corretas == 8:
        print('\33[1;33mPARABÉNS, você zerou o jogo e ganhou 1 milhão de reais!!!\33[m\n')
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