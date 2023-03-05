SalarioI = float(input('Digite o valor do seu salário: '))
aumento = SalarioI * 15 / 100
SalarioF = SalarioI + aumento

print('O seu salário de R${:.2f} com um aumento de 15% é igual a R${:.2f}'.format(SalarioI, SalarioF))

#calcula o aumento de 15% ao salário de um funcionario