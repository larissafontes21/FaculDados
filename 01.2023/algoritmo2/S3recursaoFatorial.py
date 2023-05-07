'''Recursão - exercício Fatorial

Exemplo: problema do fatorial
1) Definir o problema de forma recursiva, ou
seja, em termos dele mesmo
• n! = n * (n - 1)!
2) Definir a condição de término (ou condição
básica)
• n = 0
3) A cada chamada recursiva, deve-se tentar
garantir que se está mais próximo de
satisfazer a condição de término
• A cada chamada, n é decrementado
'''


def fat(n):   #criar função
    if n == 0:  #definir condição básica
        return 1   # 0! = 1
    else:
        res = n * fat(n-1) 
        return res
fat(5)  
