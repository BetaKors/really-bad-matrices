from matrices import Matrix
from os import system


def clear():
    system('cls || clear')


clear()

print('=' * 10 + ' Very, very bad matrix operations, by BetaKors ' + '=' * 10)

while True:
    i = input('> ')

    if i == 'cls' or i == 'clear':
        clear()
        continue

    if i == 'exit':
        break

    # converts a = {{1, 2}, {3, 4}} to (a := Matrix([[1, 2], [3, 4]]))
    operation = f'({operation})' \
                .replace('{', '[') \
                .replace('}', ']') \
                .replace('[[', 'Matrix([[') \
                .replace(']]', ']])') \
                .replace('=', ':=')

    result = eval(operation, globals(), locals())  ## yes i know this is very very very very very unsafe

    if result is not None:
        print(result)
