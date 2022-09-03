from random import randint

while True:
    n1 = str(randint(1, 100))
    n2 = str(randint(1, 100))
    
    op = '+'
    if int(n1) > int(n2):
        if randint(0, 1):
            op = '-'
    
    r = eval(n1 + op + n2)
    print('Resolva:', f'{n1} {op} {n2}', sep='\n')
    
    resp = int(input('Resposta: '))
    while resp != r:
        print('ERRADO!')
        resp = int(input('Resposta: '))

