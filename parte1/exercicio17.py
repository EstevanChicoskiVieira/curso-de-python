import random

um = input('Primeiro aluno: ')
dois = input('Segundo aluno: ')
tres = input('Terceiro aluno: ')
quatro = input('Quarto aluno: ')

lista = [um, dois, tres, quatro]
random.shuffle(lista)

print('A ordem é {}'.format(lista))

#embaralha a ordem dos alunos