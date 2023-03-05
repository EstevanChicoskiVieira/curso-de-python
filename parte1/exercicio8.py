valor = float(input('Digite o valor do produto: '))
desconto = valor * 5 / 100
total = valor - desconto

print('O valor do produto com desconto de 5% é de R${:.2f}'.format(total))

#calcula o desconto de 5% de um produto