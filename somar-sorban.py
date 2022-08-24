from random import randint

rep = ''
while rep == '':
    n1 = randint(4,9)
    n2 = randint(4,9)
    print('Some:', f'{n1} + {n2}', sep='\n')
    input('Mostrar resposta <enter>: ')
    print(n1 + n2)
    rep = input('Repetir <enter, n>? ')

