from matrices import Matrix


operation = input('Input your operation: ')

operation = operation.replace('{', '[').replace('}', ']').replace('[[', 'Matrix([[').replace(']]', ']])')

print(eval(operation, globals(), locals()))
