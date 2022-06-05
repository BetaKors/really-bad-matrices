from matrices import Matrix


def parse_operation(operation: str) -> str:
    operation = f'({operation})'
    return operation.replace('{', '[').replace('}', ']').replace('[[', 'Matrix([[').replace(']]', ']])').replace('=', ':=')


operation = ''

while operation != 'exit':
    print(eval(operation := parse_operation(input('> ')), globals(), locals()))
