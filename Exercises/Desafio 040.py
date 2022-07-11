# Crie um programa que leia duas notas de um aluno. Mostrando uma mensagem no final de acordo com a média atingida

# - Média abaixo de 5
# - Media entre 5 e 6.9
# - Média 7 ou mais voce vfoi aprovado

n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('Qual a sua segunda nota? '))
avg = (n1 + n2) / 2
if avg < 5:
    print(
        f'Infelizmente sua média foi {avg} e você foi reprovado. Estude mais na próxima vez.')
elif avg >= 5 and avg < 7:
    print(f'Na TRAVE! A sua média foi {avg} e você ficou de exame')
elif avg >= 7:
    print(
        f'Parabéns! A sua média foi {avg} e você passou direto, pode descansar!')
