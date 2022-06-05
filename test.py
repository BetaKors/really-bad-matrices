from matrices import Matrix

a = Matrix.from_rows(
    [1, 2],
    [3, 4]
)

b = Matrix.from_rows(
    [5, 6],
    [7, 8]
)

c = Matrix.from_columns(
    [1, 3],
    [2, 4]
)


def print_matrix(txt, matrix: Matrix, newline=True):
    print(txt + matrix.__str__(padding_after_first_row=len(txt)+1))

    if newline:
        print()

print_matrix('a = ', a)
print_matrix('b = ', b)
print_matrix('c = ', c)
print(f'a == c = {str(a == c).lower()}\n')
print_matrix('a + b = ', a+b)
print_matrix('a - b = ', a-b)
print_matrix('transposed a = ', a.transpose())
print_matrix('transposed b = ', b.transpose(), False)
