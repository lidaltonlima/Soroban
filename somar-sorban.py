from logging import exception
from random import randint

while True:
    n1 = str(randint(1, 100))
    n2 = str(randint(1, 100))
    
    op = '+'
    if int(n1) > int(n2):
        if randint(0, 1):
            op = '-'
    
    r = eval(n1 + op + n2)
    print('\nResolva:', f'{n1} {op} {n2}', sep='\n')
    
    resp = 0
    while not resp:
        try:
            resp = int(input('Resposta: '))
        except ValueError:
            print('Escreva um número inteiro!')
            
    while resp != r:
        print('Tente Novamente.')
        try:
            resp = int(input('Resposta: '))
        except ValueError:
            print('Escreva um número inteiro!')
    
    print('ESPLENDIDO!')

