# Estruturas de condição de uma ou duas vias

nota1 = input('Digite a nota 1: ')
nota2 = input('Digite a nota 2:')

n1 = eval(nota1)
n2 = eval(nota2)

mediaFinal = 0.4*n1 + 0.6*n2

if mediaFinal >= 5:
    print('Aprovado, sua média é ', mediaFinal)
else:
    print('Reprovado, sua média é ', mediaFinal)
