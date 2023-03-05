from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que deseja: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('\nO angulo {} tem o SENO igual a: {:.2f}'.format(angulo, seno))
print('O angulo {} tem o COSSENO igual a: {:.2f}'.format(angulo, cosseno))
print('O angulo {} tem a TANGENTE igual a: {:.2f}'.format(angulo, tangente))

#calcula o seno, o cosseno e a tangente de um angulo