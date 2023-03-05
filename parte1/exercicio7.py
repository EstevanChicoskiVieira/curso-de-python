largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

MetrosQuadrados = largura * altura
Tinta = MetrosQuadrados / 2

print('\nA quantidade necessária de tinta para pintar uma parede de {} m² é de {} litros'.format(MetrosQuadrados, Tinta))

#calcula a area de uma parede e quantos litros de tinta é necessário para pinta-la