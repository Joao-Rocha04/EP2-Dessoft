import funcoes
import math
import random
import base_questoes
jogo = True
ajudas = 2
pulos = 3
premio = 0
questoes = 1
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

while jogo == True:
    if questoes <= 3:
        nivel = 'facil'
    if 3 < questoes<= 6:
        nivel = 'medio'
    else:
        nivel = 'dificil'
    if questoes == 1:
        print('Vamos começar com questões de nível fácil!')
    if questoes==4:
        print('Está indo bem, vamos aumentar o nível das questões agora!')
    if questoes == 7:
        print('Uau! Você é bom, mas agora chegam as questões difíceis!')
    
