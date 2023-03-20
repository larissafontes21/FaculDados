altura = input('Digite a sua altura: ')
sexo = input('Digite h para homens e m para mulheres: ')

alt = eval(altura) #usar eval() pq input sempre retorna string, transformar

if sexo == 'h' :
    peso = (72.7 * alt) - 58
else:
    peso = (62.1 * alt) - 44.7

print('O peso ideal é:', peso)
