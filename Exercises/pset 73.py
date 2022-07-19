'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Sao Paulo.'''

teams = ('São Paulo', 'Fluminense', 'Botafogo', 'Inter', 'Juventude', 'Corinthians', 'Palmeiras',
         'Santos', 'Atlético Mineiro', 'Athletico Paranaense', 'Cuiabá', 'Avaí', 'Red Bull Bragantino',
         'Goiás', 'Ceará', 'Fortaleza', 'Coritiba', 'América MG', 'Atlético Goianiense', 'Flamengo')
print('-' * 30)
print(f'Os cinco primeiros times são {teams[0:6]}')
print('-' * 30)
print(f'Os últimos 4 colocados são {teams[-4:]}')
print('-' * 30)
print(f'Os times em ordem alfabética são {sorted(teams)}')
print('-' * 30)
print(f'O São Paulo está em {teams.index("São Paulo")+1}ª posição.')
