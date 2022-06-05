from matrices import Matrix
from os import system


def clear():
    system('cls || clear')
    print('=' * 10 + ' Very, very bad matrix operations, by BetaKors ' + '=' * 10)


clear()

while True:
    i = input('> ')

    if i == 'cls' or i == 'clear':
        clear()
        continue

    if i == 'exit':
        break

    result = None

    # converts a = {{1, 2}, {3, 4}} to a = Matrix([[1, 2], [3, 4]])
    operation = f'({i})' \
                .replace('{', '[') \
                .replace('}', ']') \
                .replace('[[', f'Matrix([[') \
                .replace(']]', ']])') \
                .replace('=', ':=')

    try:
        result = eval(operation)  ## yes i know this is very very very very very unsafe
    except Exception as exc:
        match exc:
            case NameError():
                result = f'`{exc.name}` doesn\'t exist!'
            case _:
                result = exc.args[0]

    if result is not None:
        print(str(result).lower())
