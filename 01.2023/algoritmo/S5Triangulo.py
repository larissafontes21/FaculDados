#Estruturas de condição de três ou mais vias
a = eval(input('Digite o lado 1:'))
b = eval(input('Digite o lado 2:'))
c = eval(input('Digite o lado 3:'))

'''maiorLado = 0

if a > maiorLado:
    maiorLado = a
if b > maiorLado:
    maiorLado = b
if c > maiorLado:
    maiorLado = c'''

maiorLado = max(a, b, c)

#Verificar se é um trinângulo
if maiorLado < a + b + c - maiorLado:
    print('É um triângulo')
    #verificar tipo do triângulo
    if a == b and b == c and a == c:
        print('Triângulo equilátero')
    elif a != b and b != c and a != c:
        print('Triângulo escaleno')
    else:
        print('Triângulo isóceles')
else:
    print('Não é um triângulo')
