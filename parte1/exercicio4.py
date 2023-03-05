num1 = int(input('Digite a Nota 1: '))
num2 = int(input('Digite a Nota 2: '))
num3 = int(input('Digite a Nota 3: '))

media = (num1 + num2 + num3) / 3

print('\n\nA média do aluno é de: {}'.format(media))

if media >= 70:
    print('O aluno está aprovado')
else:
    print('O aluno está reprovado')

#mostra a média do aluno e se ele está aprovado ou reprovado