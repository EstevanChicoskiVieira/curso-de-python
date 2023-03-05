from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hi = hypot(co, ca)

print('\nO valor da hipotenusa é de {:.3f}'.format(hi))

#calcula a hipotenusa de um triangulo retangulo