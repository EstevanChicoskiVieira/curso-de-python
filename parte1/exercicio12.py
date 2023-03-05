dias = int(input('Há quantos dias o carro foi alugado: '))
km = float(input('Qunatos Km o carro rodou: '))

diasV = dias * 60
KmV = km * 0.15

print('\n\nO valor do aluguel do carro é de R${}'.format(diasV + KmV))

#calcula o valor do aluguel de um carro
#valor por dia = 60 reais
#valor por Km rodado = 0.15 reais ou 15 centavos