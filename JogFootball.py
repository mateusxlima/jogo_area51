jogador = dict()
jogador['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))
jogador['gols'] = list()
for x in range(partidas):
    jogador['gols'].append(int(input(f'Quantos gols {jogador["Nome"]} fez na {x+1}º Partida? ')))
TotGols = 0
for x in jogador['gols']:
    TotGols += x
jogador['TotGols'] = TotGols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O compo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {TotGols} gols.')
