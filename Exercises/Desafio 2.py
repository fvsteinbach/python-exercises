print('============= Desafio 02 ==============')
dia = input('Dia de nascimento? ')
mes = input('Mês de nascimento? ')
ano = input('Ano de nascimento? ')
are_user_an_idiot = input(
    f'Você nasceu no dia {dia} de {mes} de {ano}. Correto? ')

if are_user_an_idiot == 'sim':
    confirm = input('voce é a raissa sim ou nao? ')
    if confirm == 'sim':
        print('parabens raissa')
    elif confirm == 'nao':
        print('parabens voce nao é a raissa')
    elif confirm == 'besta':
        print('qualquer coisa')
    else:
        print('erro 705')
elif are_user_an_idiot == 'nao':
    confirm = input('sim ou nao? ')
    if confirm == 'sim':
        print('parabens voce é outra pessoa')
    elif confirm == 'nao':
        print('parabens voce é a raissa')
else:
    print('erro 404')
