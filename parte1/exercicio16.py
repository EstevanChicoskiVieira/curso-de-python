import random

um = input('Primeiro aluno: ')
dois = input('Segundo aluno: ')
tres = input('Terceiro aluno: ')
quatro = input('Quarto aluno: ')

lista = [um, dois, tres, quatro]
aluno = random.choice(lista)

print('\nO aluno escolhido é {}'.format(aluno))

#ecolhe um aluno aleatório dentro da lista